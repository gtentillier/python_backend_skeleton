# Copilot Instructions — Projet Back-end Python

## 1. Contexte général du projet

- C’est un projet **Python 3.13.6** backend, l'environnement virtuel python utilisé est **.venv**.
- la variable `path_project` permet d'obtenir le chemin absolu du projet.
- la fonction `path_data(filename)` permet d'obtenir le chemin absolu du dossier 'data', en ajoutant le nom de fichier spécifié.

## 2. Normes de code et style

  - Typing strict pour les variables, arguments et résultats de fonctions, usage de `Optional[...]` plutôt que `None`.
  - Utilisation de **f-strings** pour les chaînes formatées.
  - Pas de "magic value" ni de variables globales : on paramétrise toutes les variables.
  - La logique du code doit être modulable et évolutive.
  - Fais des commentaires concis lorsque la logique du code n'est pas évidente.
  - Utilise des docstrings au format Google pour les fonctions et classes.
  - Pour la gestion de données tabulaires, usage de `pandas` :
    - `pd.DataFrame()` pour créer des DataFrames.
    - `df.to_csv(file_path, index=False)` pour sauvegarder un DataFrame en CSV.
    - `pd.read_csv(file_path)` pour lire un CSV dans un DataFrame.
    - etc.
  - Pour les chemins de fichiers/dossiers : usage de `pathlib` :
    - avec `from shared_utils import path_data, path_project` on récupère les variables `path_data` et `path_project` pour accéder aux dossiers data et racine du projet, qu'on utilise ensuite systématiquement pour indiquer des chemins vers des fichiers du projet. exemple : `file_path = path_data / "subfolder" / "file.txt"`.
    - `pathlib.Path.mkdir(parents=True, exist_ok=True)` pour créer des dossiers.
    - `pathlib.Path.exists()` pour vérifier l'existence d'un fichier/dossier.
    - `pathlib.Path.read_text(encoding="utf-8")` et `pathlib.Path.write_text(data, encoding="utf-8")` pour lire/écrire des fichiers texte.

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
│   ├── tasks
│   │   ├── _architecture.py
│   │   └── _increment_md_headers.py
│   └── utils
├── .env
├── .gitignore
├── requirements.txt
└── setup.py
```

## 4. Instructions spécifiques

Pour le mode agent :
- si tu dois exécuter un script python, utilise l'interpreteur python du projet, c'est à dire `.venv/bin/python3`
- pour les imports python, ne mets jamais de blocs try except, installe les dépendances manquantes dans l'environnement virtuel, puis suppose dans les fichiers qu'ils sont disponibles.
- Utilise les implémentations déjà existantes des fonctions/utilitaires du projet, même si elles sont dans des modules externes (exemple : Levenshtein.distance).
- Vas toujours à l'essentiel dans le code, de la manière la plus simple et concise possible, sans sacrifier la logique du code.
- Développe les modules python dans des fichiers avec des noms explicites, et importe ces fonctions via un fichier `__init__.py` dans le dossier du module.
- Ajoute toujours à la fin des scripts python un bloc `if __name__ == "__main__":` pour permettre l'exécution directe du script avec un test rapide. Il faut que le contenu de ce bloc soit minimaliste, que tous les traitements soient présents dans les fonctions du fichier.