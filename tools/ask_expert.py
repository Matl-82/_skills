#!/usr/bin/env python3
import os
import sys
import json
import asyncio
from typing import Optional
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = BASE_DIR
load_dotenv(os.path.join(BASE_DIR, ".env"))

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def list_skills():
    """Affiche la liste des experts disponibles."""
    print("\n🤖 Experts disponibles :")
    for item in os.listdir(SKILLS_DIR):
        if os.path.isdir(os.path.join(SKILLS_DIR, item)):
            meta_path = os.path.join(SKILLS_DIR, item, "metadata.json")
            if os.path.exists(meta_path):
                with open(meta_path, 'r') as f:
                    meta = json.load(f)
                    print(f"  - /{item:15} : {meta.get('description')}")
    print("\nUsage: python3 tools/ask_expert.py <expert_name> \"votre question\"\n")

def get_agent_model(expert_path: str) -> str:
    meta_path = os.path.join(expert_path, "metadata.json")
    if os.path.exists(meta_path):
        with open(meta_path, 'r') as f:
            meta = json.load(f)
            return meta.get("logic", {}).get("model", "google/gemini-2.0-flash-exp:free")
    return "google/gemini-2.0-flash-exp:free"

async def ask_expert(expert_name: str, question: str):
    """Interroge un expert spécifique."""
    expert_path = os.path.join(SKILLS_DIR, expert_name)
    prompt_path = os.path.join(expert_path, "prompts", "system_prompt.txt")

    if not os.path.exists(prompt_path):
        print(f"❌ Erreur : Expert '{expert_name}' non trouvé.")
        return

    with open(prompt_path, 'r') as f:
        system_prompt = f.read()

    model = get_agent_model(expert_path)
    print(f"⏳ Interrogation de l'expert : {expert_name} ({model})...")

    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            temperature=0.2
        )
        
        print("\n" + "="*50)
        print(f"💬 RÉPONSE DE L'EXPERT ({expert_name.upper()}) :")
        print("="*50 + "\n")
        print(response.choices[0].message.content)
        print("\n" + "="*50)

    except Exception as e:
        print(f"❌ Erreur lors de l'appel API : {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        list_skills()
    else:
        expert = sys.argv[1].replace("/", "")
        query = sys.argv[2]
        asyncio.run(ask_expert(expert, query))
