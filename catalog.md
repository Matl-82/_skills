# Bibliothèque des Agents

| Icône | Nom | Dossier | Mission |
| :--- | :--- | :--- | :--- |
| 🛡️ | **Minus v3.2** | [`minus`](minus/) | Orchestrateur — décompose, route, valide. Ne code jamais. |
| 🏗️ | **Architecte v3** | [`architecte`](architecte/) | Vision macro, trade-offs, patterns avancés (C4), blueprints Mermaid. |
| 🔨 | **Code v3** | [`code`](code/) | Implémentation pure — TDD, code incrémental, validation continue. |
| 🌐 | **Frontend v2** | [`frontend`](frontend/) | Blueprint UI + implémentation React/Next.js/Tailwind. Cycle complet. |
| ⚙️ | **Backend v2** | [`backend`](backend/) | Blueprint API + implémentation FastAPI/Node.js. Cycle complet. |
| 📱 | **iOS** | [`ios`](ios/) | Architecture iOS — Swift 6, SwiftUI, MVVM, App Store. |
| 🤖 | **Android** | [`android`](android/) | Architecture Android — Kotlin 2, Compose, MVVM/MVI. |
| 🚀 | **DevOps & CI/CD v2** | [`devops_cicd_release`](devops_cicd_release/) | Pipelines CI/CD + génération YAML/Dockerfiles/scripts. Déploiement et observabilité. |
| 📦 | **Mobile Release v2** | [`mobile_release_engineering`](mobile_release_engineering/) | Release iOS/Android — checklists stores, Fastfiles, signing. |
| 🐜 | **Debug v3** | [`debug`](debug/) | Analyse forensique, diagnostic cause racine, ordonnance de correction. |
| 🧪 | **QA Engineer v3** | [`qa_engineer`](qa_engineer/) | Stratégies de test, edge cases, garant de la non-régression. |
| 🛡️🛡️ | **Security Auditor** | [`security_auditor`](security_auditor/) | Audit sécurité web, mobile, backend — OWASP, secrets, conformité. |
| 🔍 | **Recherche** | [`recherche`](recherche/) | Veille tech, explication, documentation, rédaction technique. |
| 🪄 | **Fine Prompt** | [`fine_prompt`](fine_prompt/) | Optimisation de prompts, sélection de modèle LLM (2026). |
| 🎨 | **Design** | [`design`](design/) | Génère des prompts précis pour Claude Design — UI, illustration, brand. |

---

## Routage rapide

| Tu veux... | Agent |
|---|---|
| Choisir une architecture globale | `architecte` |
| Construire un site ou app web | `frontend` (blueprint + code) |
| Construire une API ou un backend | `backend` (blueprint + code) |
| Construire une app iPhone | `ios` |
| Construire une app Android | `android` |
| Écrire un script ou du code pur | `code` |
| Configurer une CI/CD ou un déploiement | `devops_cicd_release` |
| Publier sur l'App Store / Play Store | `mobile_release_engineering` |
| Corriger un bug | `debug` |
| Tester une feature | `qa_engineer` |
| Vérifier la sécurité | `security_auditor` |
| Comprendre un concept | `recherche` |
| Optimiser un prompt | `fine_prompt` |
| Générer un prompt visuel pour Claude Design | `design` |
| Tout ce qui précède | **`minus`** |

---

## Outils d'Exécution

| Script | Description |
| :--- | :--- |
| `tools/minus.py` | L'orchestrateur interactif. Point d'entrée principal. |
| `tools/ask_expert.py` | Pose une question isolée à un expert spécifique. |
| `tools/safe_dev_loop.py` | Boucle de développement sécurisée : Code → Test → Debug → Rollback Git automatique. |
