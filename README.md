# Faire pointer git vers le repo souhaité

```bash
git clone https://github.com/gtentillier/python_backend_skeleton.git .
git remote remove origin
git remote add origin https://github.com/gtentillier/nouveau-depot.git
git branch -m main
git add .
git commit -m 'Initial commit'
git push -u origin main
git update-index --skip-worktree .env
```

# Installation de l'environnement Python

- Cmd+T -> Créer venv
- F1, Python: Clear Workspace Interpreter Setting -> Supprimer le cache de l'environnement Python du workspace