# Faire pointer git vers le repo souhaité

```bash
git clone https://github.com/gtentillier/python_backend_skeleton.git .
git remote remove origin
git remote add origin https://github.com/gtentillier/nouveau-depot.git
git branch -m main
git add .
git commit -m 'Initial commit'
git push -u origin main
```

# Installation de l'environnement Python

- Ctrl+T -> Créer venv
- Ctrl+T -> Afficher version et localisation de Python
  - Supprimer le cache de l'environnement Python du workspace ? (F1 -> Python: Clear Workspace Interpreter Setting)

---

# Installation des Dépendances

Au démarrage du projet, exécutez les commandes suivantes pour installer les dépendances nécessaires :

```bash
pip install sqlalchemy asyncpg psycopg2-binary
pip install pydantic-settings
pip install python-jose
pip install fastapi
```
