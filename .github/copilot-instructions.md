# Copilot Instructions — Projet Back-end Python

## 1. Contexte général du projet

- C’est un projet **Python 3.13.0** backend s’appuyant sur **FastAPI**, **Pandas**, **NumPy**, **SQLAlchemy**, **Docker**, CI/CD GitHub Actions.
- l'environnement virtuel utilisé est **.venv**.

## 2. Normes de code et style

- Python :

  - Indentation à 2 espaces, imports triés, pas de wildcard imports.
  - Docstrings au format **Google**.
  - Typing strict, usage de `Optional[...]` plutôt que `None`.
  - Utilisation de **f-strings** pour les chaînes formatées.
  - Pas de variables globales.
  - code modulable et évolutif.

- FastAPI :
  - Routes organisées par **routers** dans `src/api/v1`.
  - Utilisation de **Pydantic** pour les modèles de données.

## 3. Sécurité & bonnes pratiques

- Toujours valider et nettoyer les inputs utilisateurs.
- Utiliser les mécanismes de **fastapi.Security** ou équivalent.
- Prévenir les injections SQL, XSS.
- Ajouter systématiquement **tests unitaires** sur les endpoints critiques (au moins scénario valide + scénario d’erreur).

## 4. Infrastructure & CI/CD

- Docker : chacun des services a un `Dockerfile` minimal mais optimisé.
- Docker Compose pour orchestrer les services (backend, base de données, etc.).
- Base de données : PostgreSQL, avec connexion via SQLAlchemy.
- Environnement de développement : `.env`, avec un exemple `.env.example`.
- Versioning via GitHub.
- GitHub Actions :
  - CI doit toujours faire `pytest`.
  - Deployment : staging sur `main`, prod sur `release/*`.

## 5. Architecture & modularité

- Backend → controller/routers, services, repository layers.

## 6. Tests & validation

- Génère toujours des tests via **pytest**, couvre cas positifs et négatifs.
- Si tu crées ou modifies une route API, assure-toi que des tests de response JSON et status codes sont inclus.

## 7. Communication & style

- Écrire du code clair, explicite : pas d’abréviations obscures.
- Ajouter des commentaires concis lorsque la logique est complexe.
- Pour les PR, générer un titre clair et une description listant les changements clés et l’impact.

## 8. Références & conventions internes

- Suivre la convention de nommage :
  - Backend services : `ServiceXYZ`
- Format de commit : `[<type>] <objet> – <description courte>`, type ∈ {feat, fix, chore, refactor}.

## 9. Architecture du projet :

```
├── .github
│   ├── chatmodes
│   │   └── empty.chatmode.md
│   └── copilot-instructions.md
├── .vscode
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── data
├── docker
├── docs
├── notebooks
├── src
│   ├── api
│   │   └── v1
│   ├── core
│   ├── db
│   ├── models
│   ├── repository
│   ├── services
│   └── utils
│       └── misc
├── tests
├── .env.example
├── .gitignore
├── LICENCE
├── README.md
├── architecture
└── requirements.txt
```
