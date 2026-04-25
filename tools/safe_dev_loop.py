#!/usr/bin/env python3
import os
import sys
import asyncio
import subprocess
try:
    # import dépendant de la lib `openai` (peut manquer si environnement Python non préparé)
    from minus import call_agent  # type: ignore
except ModuleNotFoundError:
    call_agent = None  # permet d'exécuter le script en mode "tests uniquement".

async def run_safe_dev_loop(task_description: str, test_command: str = "pytest", max_retries: int = 3):
    """
    Implémente le cycle: Code -> Test -> Debug -> Retry avec rollback Git.
    """
    print(f"\n🚀 Lancement de la boucle de développement sécurisée")
    print(f"📋 Tâche : {task_description}")
    print(f"🧪 Commande de test : {test_command}")
    
    # 1. Backup via Git
    print("\n📦 Étape 1 : Création du point de sauvegarde (Git commit temporaire)...")
    try:
        # S'assure qu'on est dans un repo git
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], check=True, capture_output=True)

        # Commit de backup : on préfère créer un commit même s'il n'y a rien à sauvegarder.
        # (Le rollback sera alors un reset HEAD~1 cohérent.)
        subprocess.run(["git", "add", "-A"], check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", "backup_before_task_safe_dev_loop"],
            check=True,
            capture_output=True,
        )
        print("✅ Sauvegarde réussie (backup_before_task_safe_dev_loop).")
    except subprocess.CalledProcessError:
        print("❌ Erreur : Le dossier actuel n'est pas un dépôt Git ou le commit a échoué.")
        print("Veuillez initialiser git ('git init') pour utiliser le mécanisme de rollback.")
        return False

    context = ""
    attempt = 1

    if call_agent is None:
        print("❌ Dépendance LLM indisponible : module 'openai' manquant. Installe `openai` dans l'environnement Python utilisé ou exécute avec un venv configuré.")
        return False

    while attempt <= max_retries:
        print(f"\n🔄 --- TENTATIVE {attempt}/{max_retries} ---")
        
        # 2. Appel Agent Code
        print("👨‍💻 Étape 2 : L'agent Code travaille...")
        code_result = await call_agent("code", task_description, context)
        print("✅ Code généré.")
        
        # 3. Exécution Tests
        print(f"🧪 Étape 3 : Exécution des tests ('{test_command}')...")
        process = subprocess.run(test_command, shell=True, capture_output=True, text=True)
        
        # 4. Évaluation
        if process.returncode == 0:
            print("✅ SUCCÈS : Les tests passent ! La boucle est terminée.")
            # Optionnel : On pourrait squasher le commit de backup ici ou le garder.
            # Pour l'instant, on laisse le commit de backup tel quel + les nouveaux changements en unstaged/staged.
            return True
        else:
            print("❌ ÉCHEC : Les tests ont échoué.")
            error_output = f"Code de retour: {process.returncode}\n\nSTDOUT:\n{process.stdout}\n\nSTDERR:\n{process.stderr}"
            
            if attempt == max_retries:
                break # On sort de la boucle pour faire le rollback
            
            print("🐛 Étape 4 : L'agent Debug analyse l'erreur...")
            debug_task = f"Les tests ont échoué lors de l'implémentation de la tâche suivante:\n{task_description}\n\nVoici la sortie d'erreur des tests:\n{error_output}"
            debug_result = await call_agent("debug", debug_task, "Trouve la cause racine de l'échec des tests.")
            
            # Mise à jour du contexte pour le prochain tour de l'agent code
            context += f"\n\n--- Tentative {attempt} échouée ---\nAnalyse de l'agent Debug :\n{debug_result}\n\nCorrige le code en fonction de cette analyse."
            attempt += 1

    # 5. Rollback (si on arrive ici, c'est que max_retries est atteint et returncode != 0)
    print(f"\n⚠️ ÉCHEC DÉFINITIF après {max_retries} tentatives.")
    print("⏪ Étape 5 : Restauration de la sauvegarde (Rollback Git)...")
    try:
        subprocess.run(["git", "reset", "--hard", "HEAD~1"], check=True, capture_output=True)
        print("✅ Restauration réussie. Le projet est revenu à son état initial.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur critique lors du rollback : {e}")
    
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python safe_dev_loop.py \"Description de la tâche\" [\"commande de test\"]")
        sys.exit(1)
        
    task = sys.argv[1]
    cmd = sys.argv[2] if len(sys.argv) > 2 else "pytest"
    
    asyncio.run(run_safe_dev_loop(task, cmd))
