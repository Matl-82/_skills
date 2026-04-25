# 🧠 Bibliothèque de Skills

Ce dossier contient les "cerveaux" modulaires des agents IA. Chaque dossier représente une compétence spécifique (Skill) dotée de sa propre identité, de ses capacités et de sa logique.

## 🛠 Standard de Conception
Tous les skills suivent une structure normalisée :
- `metadata.json` : Identité, version, capacités et configuration technique.
- `prompts/system_prompt.txt` : Instructions système et missions de l'agent.

## 🛡 Minus
L'ensemble des agents de cette bibliothèque est régi par **Minus**. Ce protocole garantit :
1. **Discipline** : Une boucle d'exécution en 7 étapes pour chaque tâche.
2. **Apprentissage** : La capitalisation systématique des erreurs dans `minus/_memory/erreurs_apprises.md`.
3. **Preuve** : Une obligation de validation concrète avant de considérer une tâche comme terminée.

---

## 📚 Catalogue des Rôles
Pour une vue détaillée des experts disponibles, consultez la [Bibliothèque des Rôles](catalog.md).
