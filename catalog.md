# 📖 Bibliothèque des Rôles (Skills Catalog)

Bienvenue dans la bibliothèque des agents. Chaque expert listé ci-dessous peut être invoqué pour des tâches spécifiques.

| Icone | Nom du Rôle | Dossier | Mission Principale |
| :--- | :--- | :--- | :--- |
| 🛡️ | **Master Protocol** | [`master_protocol`](master_protocol/) | Standard global d'exécution et d'apprentissage continu. |
| 💼 | **Chef de Projet** | [`chef_de_projet`](chef_de_projet/) | Analyse, décomposition et routage des tâches complexes. |
| 🏗️ | **Architecte** | [`architecte`](architecte/) | Vision macro, choix technologiques et structure système. |
| 🔨 | **Codeur** | [`code`](code/) | Implémentation disciplinée et tests de fonctionnalités. |
| 🐜 | **Debugger** | [`debug`](debug/) | Analyse forensique et corrections chirurgicales. |
| 🪄 | **Fine Prompt** | [`fine_prompt`](fine_prompt/) | Optimisation des interactions et sélection des LLM. |
| 🛡️🛡️ | **Sec Auditor** | [`security_auditor`](security_auditor/) | Audit de sécurité, vulnérabilités et conformité. |
| 🧪 | **QA Engineer** | [`qa_engineer`](qa_engineer/) | Stratégie de test, edge cases et robustesse. |
| 🔍 | **Recherche** | [`recherche`](recherche/) | Synthèse d'information, vulgarisation et documentation. |
| 🎨 | **Stitch Design** | [`stitch-design`](stitch-design/) | Expert Design Systems et génération d'UI via Stitch MCP. |
| 🔄 | **Stitch Loop** | [`stitch-loop`](stitch-loop/) | Gestion itérative de projets Design multi-écrans. |
| 📚 | **Design MD** | [`design-md`](design-md/) | Création de la source de vérité design (.stitch/DESIGN.md). |

---

## 📋 Détails des Capacités

### [Architecte](architecte/metadata.json)
- Conception de systèmes (Monolithe, Microservices).
- Évaluation technique d'outils et bibliothèques.
- Standardisation (nommage, sécurité, documentation).

### [Chef de Projet](chef_de_projet/metadata.json)
- Décomposition de roadmap.
- Routage intelligent vers les experts (/architecte, /code, /debug).
- Vérification de la cohérence globale.

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

### [Stitch Design](stitch-design/metadata.json)
- Expert Lead Design et Prompt Engineering UI/UX.
- Génération et édition de maquettes via Stitch MCP.
- Maintenance de la cohérence visuelle.

### [Stitch Loop](stitch-loop/metadata.json)
- Orchestration de workflows design complexes.
- Gestion des versions et des variantes d'écrans.

### [Design MD](design-md/metadata.json)
- Synthèse de "Source of Truth" design.
- Documentation des tokens, couleurs et typographies.

---

## 🚦 Routage Intelligent (Triggers Négatifs)
Tous les skills intègrent désormais des `negative_triggers` dans leur `metadata.json`. Cela permet d'affiner la sélection automatique de l'agent en définissant explicitement ce qu'il **ne doit pas** faire.
