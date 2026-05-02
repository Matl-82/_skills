# 📖 Bibliothèque des Agents

| Icône | Nom | Dossier | Mission |
| :--- | :--- | :--- | :--- |
| 🛡️ | **Minus v3** | [`minus`](minus/) | Orchestrateur Élite — CoT, routage intelligent, validation empirique. |
| 🏗️ | **Architecte v3** | [`architecte`](architecte/) | Vision macro, trade-offs, patterns avancés (C4), blueprints Mermaid. |
| 🔨 | **Code v3** | [`code`](code/) | Ingénierie suprême — TDD, implémentation incrémentale, validation continue. |
| 🌐 | **Frontend** | [`frontend`](frontend/) | Spécifications UI Web, Core Web Vitals, accessibilité. |
| ⚙️ | **Backend** | [`backend`](backend/) | Spécifications API REST/GraphQL, schémas DB, auth enterprise. |
| 📱 | **iOS** | [`ios`](ios/) | Spécifications iOS — Swift 6, SwiftUI, MVVM, App Store. |
| 🤖 | **Android** | [`android`](android/) | Spécifications Android — Kotlin 2, Compose, MVVM/MVI. |
| 🐜 | **Debug v3** | [`debug`](debug/) | Analyse forensique, diagnostic cause racine, ordonnance de correction. |
| 🧪 | **QA Engineer v3** | [`qa_engineer`](qa_engineer/) | Stratégies impitoyables, edge cases, garant de la non-régression. |
| 🛡️🛡️ | **Security Auditor** | [`security_auditor`](security_auditor/) | Audit sécurité web, mobile, backend — OWASP, secrets, conformité. |
| 🔍 | **Recherche** | [`recherche`](recherche/) | Veille tech, explication, documentation, rédaction technique. |
| 🪄 | **Fine Prompt** | [`fine_prompt`](fine_prompt/) | Optimisation de prompts, sélection de modèle LLM (2026). |
| 🎨 | **Design** | [`design`](design/) | (NO CODE) Génère des prompts pour Claude Design — UI, illustration, brand. |
| 🧩 | **Web UI Blueprint** | [`web_ui_blueprint`](web_ui_blueprint/) | (NO CODE) Architecture UI Web, routing, state management. |
| 🚀 | **DevOps & Release** | [`devops_cicd_release`](devops_cicd_release/) | (NO CODE) Pipelines CI/CD, stratégies de déploiement, observabilité. |
| 🏢 | **Backend Enterprise** | [`backend_web_enterprise`](backend_web_enterprise/) | (NO CODE) API complexes, auth enterprise, migrations DB. |
| 📦 | **Mobile Release** | [`mobile_release_engineering`](mobile_release_engineering/) | (NO CODE) Checklists stores, signature, release automation mobile. |

---

## Routage rapide

| Tu veux... | Agent |
|---|---|
| Savoir quelle architecture choisir | `architecte` |
| Concevoir l'architecture Web UI (sans coder) | `web_ui_blueprint` |
| Concevoir des API/BDD complexes (sans coder) | `backend_web_enterprise` |
| Construire un site ou app web (code) | `frontend` + `backend` |
| Planifier une release mobile (stores) | `mobile_release_engineering` |
| Construire une app iPhone (code) | `ios` |
| Construire une app Android (code) | `android` |
| Écrire un script Python | `code` |
| Planifier une CI/CD ou un déploiement | `devops_cicd_release` |
| Corriger un bug | `debug` |
| Tester une feature | `qa_engineer` |
| Vérifier la sécurité | `security_auditor` |
| Comprendre un concept | `recherche` |
| Optimiser un prompt | `fine_prompt` |
| Générer un prompt visuel pour Claude Design | `design` |
| Tout ce qui précède | **`minus`** |
| Développer en boucle sécurisée | `safe_dev_loop` |

---

## 🛠️ Outils d'Exécution

| Script | Description |
| :--- | :--- |
| `tools/minus.py` | L'orchestrateur interactif. Le point d'entrée principal pour discuter avec Minus. |
| `tools/ask_expert.py` | Pose une question isolée à un expert spécifique (ex: `python3 tools/ask_expert.py ios "Comment faire..."`). |
| `tools/safe_dev_loop.py` | Boucle de développement sécurisée : Code -> Test -> Debug -> Rollback Git automatique en cas d'échec. |
