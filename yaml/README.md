# 🎯 Roo Code Custom Modes - 17 Rôles Spécialisés

Ce dossier contient **17 fichiers YAML** (un par rôle) pour configurer Roo Code avec une architecture **Code-centric** : seul `Code` peut modifier du code, tous les autres rôles fournissent des specs/blueprints.

---

## 📋 Structure des Fichiers

```
yaml/
├── 01_minus.yaml              ← Orchestrateur (lecture seule)
├── 02_code.yaml               ← Code (seul qui écrit)
├── 03_architecte.yaml         ← Architecture (blueprints)
├── 04_frontend.yaml           ← Frontend Web (specs)
├── 05_backend.yaml            ← Backend API (specs)
├── 06_ios.yaml                ← iOS (specs)
├── 07_android.yaml            ← Android (specs)
├── 08_debug.yaml              ← Debug (diagnostic)
├── 09_qa_engineer.yaml        ← QA (plans de test)
├── 10_security_auditor.yaml   ← Sécurité (recommandations)
├── 11_recherche.yaml          ← Recherche (explication)
├── 12_fine_prompt.yaml        ← Prompts (optimisation)
├── 13_design.yaml             ← Design (specs visuelles)
├── 14_web_ui_blueprint.yaml   ← Web UI (blueprints)
├── 15_backend_enterprise.yaml ← Backend complex (blueprints)
├── 16_devops.yaml             ← DevOps (pipelines)
├── 17_mobile_release.yaml     ← Mobile release (checklists)
└── README.md                  ← Ce fichier
```

---

## 🚀 Comment Utiliser

### Option 1️⃣ : Charger tous les rôles à la fois

1. **Ouvrez VSCode**
2. **Cmd+Shift+P** → `Roo: Edit Global Modes`
3. **Copiez et collez** le contenu de chaque fichier **dans l'ordre** (01 → 17)
4. **Sauvegardez** et redémarrez VSCode

### Option 2️⃣ : Charger un rôle à la fois (recommandé pour débuter)

1. **Ouvrez le fichier YAML** que vous voulez (ex: `02_code.yaml`)
2. **Copiez le contenu**
3. **Dans VSCode**, Cmd+Shift+P → `Roo: Edit Global Modes`
4. **Remplacez ou ajoutez** le contenu
5. **Sauvegardez**

---

## 🎯 Architecture des Rôles

| Rôle | Permissions | Fonction |
|------|-------------|----------|
| **🛡️ Minus** | read, command, mcp | Orchestration, coordination |
| **🔨 Code** | read, **edit**, command, mcp | ⭐ **SEUL qui code** |
| **🏗️ Architecte** | read, command, mcp | Architecture & blueprints |
| **🌐 Frontend** | read, command, mcp | Architecture UI web |
| **⚙️ Backend** | read, command, mcp | Architecture API & données |
| **📱 iOS** | read, command, mcp | Architecture iOS |
| **🤖 Android** | read, command, mcp | Architecture Android |
| **🐜 Debug** | read, command, mcp | Diagnostic & specs de fix |
| **🧪 QA** | read, command, mcp | Plans de test |
| **🛡️ Security** | read, command, mcp | Recommandations sécurité |
| **🔍 Recherche** | read, command, mcp | Explication & documentation |
| **🪄 Fine Prompt** | read, command, mcp | Optimisation prompts |
| **🎨 Design** | read, command, mcp | Specs visuelles |
| **🧩 Web UI** | read, command, mcp | Blueprints UI web |
| **🏢 Backend Ent.** | read, command, mcp | Blueprints backend complexe |
| **🚀 DevOps** | read, command, mcp | Pipelines CI/CD |
| **📦 Mobile Release** | read, command, mcp | Checklists stores |

---

## 📌 Flux de Travail Recommandé

```
1. Utilisateur demande une tâche complexe
   ↓
2. Minus (orchestrateur) analyse & décompose
   ↓
3. Spécialistes (Architecte, Frontend, Backend, etc.) proposent leurs blueprints
   ↓
4. Code reçoit TOUS les blueprints + specs précises
   ↓
5. Code SEUL implémente exactement ce qui est demandé
   ↓
6. QA & Security valident
   ↓
7. Debug corrige si besoin
```

---

## ⚡ LLM Recommandé pour Chaque Rôle

- **Minus** → GPT-5.5 (orchestration)
- **Code** → Claude Opus 4.7 (puissance maximale)
- **Architecte** → Gemini 3.1 Pro (vision macro)
- **Frontend/iOS/Android** → Qwen 3 Coder (code mobile/web)
- **Backend** → Qwen 3.6 Plus (données & APIs)
- **Debug** → DeepSeek v4 Pro (logique profonde)
- **Security** → DeepSeek v4 Pro (expertise sécurité)
- **Recherche** → Gemini 3.1 Pro (synthèse)
- **Fine Prompt** → DeepSeek v4 Pro (optimisation)
- **Design** → Claude Sonnet 4.6 (créativité)
- **Others** → Gemini 3.1 Pro (blueprints)

---

## 🔧 Dépannage

**Les modes n'apparaissent pas ?**
1. Fermez VSCode complètement
2. Supprimer le cache : `rm -rf ~/Library/Application\ Support/Code/User/globalStorage/roovetiarinyinc.roo-cline/`
3. Rouvrez VSCode
4. Réintégrez les modes YAML

**Erreur de YAML ?**
- Vérifiez l'indentation (2 espaces, pas de tabs)
- Assurez-vous que `customModes:` est à la ligne 1

---

## 📝 Notes

- Chaque fichier est **indépendant** et peut être utilisé seul
- Les permissions `edit` sont **UNIQUEMENT pour Code**
- Les autres rôles ont `read, command, mcp` (lecture seule)
- Les specs doivent être **précises et détaillées** pour que Code les implémente correctement

---

**Bon usage ! 🚀**
