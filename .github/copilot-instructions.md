# Copilot Instructions — Projet Back-end Python

## 1. Contexte général du projet

- C’est un projet **Python 3.13.6** backend, l'environnement virtuel python utilisé est **.venv**.
- la variable `path_project` permet d'obtenir le chemin absolu du projet.
- la fonction `path_data(filename)` permet d'obtenir le chemin absolu du dossier 'data', en ajoutant le nom de fichier spécifié.
- Utilise l'environnementy virtuel situé à la racine du projet : `.venv/bin/python3`.

## 2. Normes de code et style

  - Typing strict pour les variables, arguments et résultats de fonctions, usage de '|' : `class_1 | class_2 | None` par exemple plutôt que `Optional[...]`. Pour le typing des variables incluant des listes ou des dictionnaires, utilise `list[...]` et `dict[...]` plutôt que `List[...]` et `Dict[...]`.
  - Ne mets pas de variables mutables en valeurs par défaut des arguments de fonctions (exemple : listes, dictionnaires, ensembles).
  - Ne garde pas d'imports inutilisés.
  - Utilisation de **f-strings** pour les chaînes formatées.
  - Utilisation de time.perf_counter() pour mesurer les performances et les durées d'exécution de lignes de code.
  - Pas de "magic value" ni de variables globales : on paramétrise toutes les variables.
  - La logique du code doit être modulable et évolutive.
  - Fais des commentaires concis lorsque la logique du code n'est pas évidente.
  - Utilise des docstrings au format Google pour les fonctions et classes.
  - Ne fais pas de tests unitaires.

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

  - Pour définir le device pytorch utilisé, utilise `device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")`.

  - Utilisation de `@dataclass` et `__post_init__`
    - Quand tu définis des classes, **utilise le décorateur `@dataclass`**.
    - * Utilise `@dataclass` pour éviter d’écrire manuellement les méthodes `__init__`, `__repr__`, et `__eq__`.
    - * Si une logique doit être exécutée après l’initialisation (par exemple validation, calcul de champs dérivés, transformation de valeurs), place-la dans une méthode `__post_init__(self)` plutôt que de redéfinir `__init__`.
    - * Ne redéfinis `__init__` **que si c’est strictement nécessaire** (ex. initialisation conditionnelle complexe non compatible avec `__post_init__`).
    - * Préfère l’utilisation de `field(default=...)` ou `field(default_factory=...)` pour les valeurs par défaut dynamiques.
    - * Si une propriété ne doit pas être initialisée via le constructeur, définis-la avec `init=False` et initialise-la dans `__post_init__`.
    - * Garde les classes **lisibles, déclaratives et auto-documentées** : privilégie des annotations de type claires et des noms de champs explicites.

    **Exemple attendu :**

    ```python
    from dataclasses import dataclass, field

    @dataclass
    class Produit:
        nom: str
        prix_unitaire: float
        quantite: int = 1
        total: float = field(init=False)

        def __post_init__(self):
            if self.prix_unitaire < 0:
                raise ValueError("Le prix ne peut pas être négatif.")
            self.total = self.prix_unitaire * self.quantite
    ```

  - Pour mesurer la durée d'exécution d'une brique de code, utilise le décorateur de fonction `measure_time`. L'import se fait comme ceci : `from shared_utils import measure_time`. `measure_time` se place directement au-dessus de la fonction concernée, calcule la durée avec `time.perf_counter()`, et affiche le résultat formaté : 

  ```python
  from shared_utils import measure_time

  @measure_time
  def traitement_principal() -> None:
      # ...logic...
      pass
  ```

  - pour un appel OpenAI, importe `OpenAILLMCaller` ou `OpenAISTTCaller`, et `PricingCalculator` et logue toujours `price.display()`. L'import est le suivant : `from shared_utils import OpenAILLMCaller, OpenAISTTCaller, PricingCalculator`. Les prix peuvent être ajoutés natuerellement entre eux pour garder un suivi des prix d'un enchaînement de requêtes. l’exemple suivant montre la requête, le calcul de coût et l’affichage du prix de la réponse :

  ```python
  from shared_utils import OpenAILLMCaller, PricingCalculator

  def requete_openai(prompt: str, api_key: str, verbose: bool = False) -> str:
      caller = OpenAILLMCaller(api_key=api_key)
      response = caller.response(model="gpt-4.1-nano", input=prompt, max_output_tokens=128)
      if verbose:
        prix = PricingCalculator().get_price(response, stt_model_name=None)
        prix.display()
      return response.output_text
  ```

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
- réserve les blocs try except aux endroits où une erreur est possible, pour gérer des exceptions qui surviendront, mais pas au cas où pour des erreurs qu'on n'est pas censé rencontrer dans le cadre normal du programme.
- ne vérifie pas l'existence de fichiers/dossiers systématiquement, s'ils sont déjà censés exister tu peux supposer qu'ils existent pour ne pas alourdir le code. si tu utilises un dossier, tu peux quand même vérifier son existence et le créer si besoin avec `pathlib.Path.mkdir(parents=True, exist_ok=True)`.