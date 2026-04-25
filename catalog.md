# 📖 Bibliothèque des Rôles (Skills Catalog)

Bienvenue dans la bibliothèque des agents. Chaque expert listé ci-dessous peut être invoqué pour des tâches spécifiques.

| Icone | Nom du Rôle | Dossier | Mission Principale |
| :--- | :--- | :--- | :--- |
| 🛡️ | **Minus** | [`minus`](minus/) | Orchestrateur principal : décomposition, routage, exécution disciplinée et apprentissage continu. |
| 🏗️ | **Architecte** | [`architecte`](architecte/) | Vision macro, choix technologiques et structure système. |
| 🔨 | **Codeur** | [`code`](code/) | Implémentation disciplinée et tests de fonctionnalités. |
| 🐜 | **Debugger** | [`debug`](debug/) | Analyse forensique et corrections chirurgicales. |
| 🪄 | **Fine Prompt** | [`fine_prompt`](fine_prompt/) | Optimisation des interactions et sélection des LLM. |
| 🛡️🛡️ | **Sec Auditor** | [`security_auditor`](security_auditor/) | Audit de sécurité, vulnérabilités et conformité. |
| 🧪 | **QA Engineer** | [`qa_engineer`](qa_engineer/) | Stratégie de test, edge cases et robustesse. |
| 🔍 | **Recherche** | [`recherche`](recherche/) | Synthèse d'information, vulgarisation et documentation. |

---

## 📋 Détails des Capacités

### [Architecte](architecte/metadata.json)
- Conception de systèmes (Monolithe, Microservices).
- Évaluation technique d'outils et bibliothèques.
- Standardisation (nommage, sécurité, documentation).

### [Minus](minus/metadata.json)
- Décomposition de roadmap et création de feuilles de route.
- Routage intelligent vers les experts (architecte, code, debug, qa_engineer, security_auditor, recherche, fine_prompt).
- Exécution disciplinée via la boucle en 7 étapes.
- Capitalisation des erreurs dans `minus/_memory/erreurs_apprises.md`.

### [Codeur](code/metadata.json)
- Implémentation incrémentale.
- Preuve par le test.
- Capitalisation des erreurs.

### [Debugger](debug/metadata.json)
- Analyse de logs et Root Cause Analysis.
- Corrections chirurgicales (fixes minimaux).

### [Fine Prompt](fine_prompt/metadata.json)
- Optimisation de prompts (CoT, Few-Shot).
- Recommandation de modèles (Claude, Gemini, DeepSeek, etc.).

### [Recherche](recherche/metadata.json)
- Vulgarisation de concepts complexes.
- Analyse documentaire sans modification.
- Rédaction technique (README, Doc).

### [Security Auditor](security_auditor/metadata.json)
- Scan de vulnérabilités (OWASP).
- Audit des protocoles d'authentification.
- Gestion sécurisée des secrets.

### [QA Engineer](qa_engineer/metadata.json)
- Planification de tests (Unitaires, Intégration, E2E).
- Identification de cas limites (Edge Cases).
- Tests de régression.

---

## 🚦 Routage Intelligent (Triggers Négatifs)
Tous les skills intègrent désormais des `negative_triggers` dans leur `metadata.json`. Cela permet d'affiner la sélection automatique de l'agent en définissant explicitement ce qu'il **ne doit pas** faire.
