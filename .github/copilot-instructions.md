# Copilot Instructions — Projet Back-end Python

## 1. Contexte général du projet

- C’est un projet **Python 3.13.6** backend, l'environnement virtuel python utilisé est **.venv**.
- la variable 'path_project' permet d'obtenir le chemin absolu du projet.
- la fonction 'path_data(<filename>)' permet d'obtenir le chemin absolu du dossier 'data', en ajoutant le nom de fichier spécifié.

## 2. Normes de code et style

  - Typing strict pour les variables, arguments et résultats de fonctions, usage de `Optional[...]` plutôt que `None`.
  - Utilisation de **f-strings** pour les chaînes formatées.
  - Pas de "magic value" ni de variables globales : on paramétrise toutes les variables.
  - La logique du code doit être modulable et évolutive.
  - Fais des commentaires concis lorsque la logique du code n'est pas évidente.
  - Utilise des docstrings au format Google pour les fonctions et classes.

## 3. Architecture du projet :

```
├── data
├── docker
├── docs
├── src
│   ├── api
│   │   └── users.py
│   ├── db
│   │   └── session.py
│   ├── modules
│   │   ├── core
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── module_1
│   │   ├── module_2
│   │   └── shared
│   └── utils
│       ├── get_architecture.py
│       └── get_paths.py
├── .env
├── .gitignore
├── requirements.txt
└── setup.py
```