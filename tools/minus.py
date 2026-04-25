#!/usr/bin/env python3
"""
Minus — Orchestrateur IA personnel de TeuTeu
"""
import os
import json
import asyncio
import re
from datetime import datetime
from pathlib import Path
from openai import AsyncOpenAI, RateLimitError
from dotenv import load_dotenv

# Chemins
SKILLS_DIR = Path(__file__).parent.parent
MINUS_DIR  = SKILLS_DIR / "minus"
MEMORY_DIR = MINUS_DIR / "_memory"
SYSTEM_PROMPT_PATH = MINUS_DIR / "prompts" / "system_prompt.txt"

# Cherche le .env à la racine du projet
load_dotenv(SKILLS_DIR.parent / ".env")
load_dotenv(SKILLS_DIR / ".env")

MODEL          = os.getenv("MODEL",          "google/gemini-2.5-pro-exp-03-25:free")
MODEL_FALLBACK = os.getenv("MODEL_FALLBACK", "deepseek/deepseek-chat-v3-0324:free")

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# ──────────────────────────────────────────────
# APPEL LLM AVEC FALLBACK AUTOMATIQUE
# ──────────────────────────────────────────────

async def chat(messages: list, temperature: float = 0.0) -> str:
    model = MODEL
    for attempt in range(2):
        try:
            response = await client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message.content
        except RateLimitError:
            if attempt == 0:
                print(f"   ⚠️  Rate limit sur {model}, bascule sur {MODEL_FALLBACK}...")
                model = MODEL_FALLBACK
            else:
                raise

# ──────────────────────────────────────────────
# MÉMOIRE
# ──────────────────────────────────────────────

def load_memory() -> str:
    profil  = MEMORY_DIR / "profil.md"
    erreurs = MEMORY_DIR / "erreurs_apprises.md"
    context = ""
    if profil.exists():
        context += f"\n## PROFIL\n{profil.read_text()}\n"
    if erreurs.exists():
        context += f"\n## ERREURS APPRISES\n{erreurs.read_text()}\n"
    return context

def load_system_prompt() -> str:
    system = SYSTEM_PROMPT_PATH.read_text()
    memory = load_memory()
    if memory:
        system += f"\n\n---\n\n## MÉMOIRE CHARGÉE EN DÉBUT DE SESSION\n{memory}"
    return system

def apply_memory_updates(updates: list[dict]):
    file_map = {
        "profil":  MEMORY_DIR / "profil.md",
        "erreurs": MEMORY_DIR / "erreurs_apprises.md",
    }
    for u in updates:
        path = file_map.get(u["file"])
        if path and u["content"].strip():
            with open(path, "a") as f:
                f.write(f"\n\n<!-- {datetime.now().strftime('%Y-%m-%d')} -->\n")
                f.write(u["content"].strip() + "\n")

# ──────────────────────────────────────────────
# PARSING
# ──────────────────────────────────────────────

def parse_delegates(text: str) -> list[dict]:
    matches = re.findall(r'\[DELEGATE\]\s*(.*?)\s*\[/DELEGATE\]', text, re.DOTALL)
    result = []
    for m in matches:
        try:
            result.append(json.loads(m))
        except json.JSONDecodeError:
            pass
    return result

def parse_memory_updates(text: str) -> list[dict]:
    matches = re.findall(r'\[MEMORY_UPDATE:(\w+)\]\s*(.*?)\s*\[/MEMORY_UPDATE\]', text, re.DOTALL)
    return [{"file": f, "content": c} for f, c in matches]

def strip_blocks(text: str) -> str:
    text = re.sub(r'\[DELEGATE\].*?\[/DELEGATE\]', '', text, flags=re.DOTALL)
    text = re.sub(r'\[MEMORY_UPDATE:\w+\].*?\[/MEMORY_UPDATE\]', '', text, flags=re.DOTALL)
    return text.strip()

# ──────────────────────────────────────────────
# AGENTS
# ──────────────────────────────────────────────

async def call_agent(agent_name: str, task: str, context: str) -> str:
    prompt_path = SKILLS_DIR / agent_name / "prompts" / "system_prompt.txt"
    if not prompt_path.exists():
        return f"❌ Agent '{agent_name}' introuvable."
    print(f"   ↳ [{agent_name}] en cours...")
    return await chat(
        messages=[
            {"role": "system", "content": prompt_path.read_text()},
            {"role": "user",   "content": f"{context}\n\nTâche : {task}".strip()}
        ],
        temperature=0.2
    )

# ──────────────────────────────────────────────
# TRAITEMENT DE LA RÉPONSE
# ──────────────────────────────────────────────

async def process(text: str, history: list, system: str) -> str:
    memory_updates = parse_memory_updates(text)
    if memory_updates:
        apply_memory_updates(memory_updates)

    delegates = parse_delegates(text)
    clean = strip_blocks(text)

    if delegates:
        print(f"\n🔀 Minus délègue à {len(delegates)} agent(s)...")
        results = []
        for d in delegates:
            result = await call_agent(d.get("agent", ""), d.get("task", ""), d.get("context", ""))
            results.append(f"### Résultat de [{d.get('agent')}]\n{result}")

        injection = "\n\n".join(results)
        history.append({"role": "assistant", "content": clean or "Je délègue."})
        history.append({"role": "user", "content": f"[RÉSULTATS_AGENTS]\n{injection}\n[/RÉSULTATS_AGENTS]\n\nSynthétise et réponds à TeuTeu."})

        final = await chat(
            messages=[{"role": "system", "content": system}] + history,
            temperature=0.0
        )
        mu = parse_memory_updates(final)
        if mu:
            apply_memory_updates(mu)
        return strip_blocks(final)

    return clean

# ──────────────────────────────────────────────
# FIN DE SESSION
# ──────────────────────────────────────────────

async def end_session(history: list, system: str):
    if len(history) < 2:
        return

    prompt = """Fin de session. Analyse notre échange.

Si tu as appris quelque chose de nouveau sur TeuTeu, mets à jour son profil :
[MEMORY_UPDATE:profil]
ce qui change ou s'ajoute au profil
[/MEMORY_UPDATE]

Si une erreur ou une leçon est à retenir, documente-la :
[MEMORY_UPDATE:erreurs]
## [Catégorie]
### [Titre]
- **Date** : YYYY-MM-DD
- **Contexte** : ...
- **Erreur** : ...
- **Correction** : ...
- **Règle** : ...
[/MEMORY_UPDATE]

Si rien de nouveau : réponds uniquement RIEN."""

    content = await chat(
        messages=[{"role": "system", "content": system}] + history + [
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )
    if content.strip().upper() != "RIEN":
        updates = parse_memory_updates(content)
        if updates:
            apply_memory_updates(updates)
            print(f"\n💾 Mémoire mise à jour ({len(updates)} fichier(s))")

# ──────────────────────────────────────────────
# BOUCLE PRINCIPALE
# ──────────────────────────────────────────────

async def main():
    system  = load_system_prompt()
    history = []

    print("\n" + "═"*50)
    print(f"⚡  MINUS — En ligne  [{MODEL}]")
    print("═"*50)
    print("  tape 'exit' pour quitter\n")

    while True:
        try:
            user_input = input("TeuTeu → ").strip()
        except (KeyboardInterrupt, EOFError):
            user_input = "exit"

        if user_input.lower() in ("exit", "quit", "bye", "ciao"):
            print("\n⏳ Sauvegarde de la session...")
            await end_session(history, system)
            print("Minus → À plus TeuTeu. 🤙\n")
            break

        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})

        try:
            raw   = await chat([{"role": "system", "content": system}] + history)
            reply = await process(raw, history, system)
            history.append({"role": "assistant", "content": reply})
            print(f"\nMinus → {reply}\n")

        except Exception as e:
            print(f"\n❌ Erreur : {e}\n")


if __name__ == "__main__":
    asyncio.run(main())
