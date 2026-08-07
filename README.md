
# Code Cultivation — POO (Python) @ 42

🪴 Projet de POO en Python — collection d'exercices et d'énoncés pour les modules P0 → P3 (Module 1 @ 42 Antananarivo). Ce dépôt sert de support d'apprentissage pour la programmation orientée objet en Python : conception d'un écosystème de plantes, encapsulation, héritage, fabriques d'objets dynamiques et suivi analytique. Validé selon PEP 8 et typage statique.

## Table of contents
- [What this is](#what-this-is)
- [Structure](#structure)
- [Requirements](#requirements)
- [How to run an exercise](#how-to-run-an-exercise)
- [Coding standards](#coding-standards)
- [Resources (exercise subjects)](#resources-exercise-subjects)
- [Contributing](#contributing)
- [Notes](#notes)

## What this is
A structured set of Python exercises and subjects used to learn and demonstrate object-oriented design patterns and practices at 42. Each `Pn` directory groups exercises and the official subject PDF for that module.

## Structure
Top-level layout (annotated):

```
P0/            # Module P0: subject PDF + small exercises (ex0..ex7)
P1/            # Module P1: subject PDF + exercises (ex0..ex6)
P2/            # Module P2: exercises (ex0..ex4)
P3/            # Module P3: exercises (ex0..ex6) + module3.pdf
P4/            # Modulea P4
```

Inside each `Pn`:
- `en.subject.pdf` or `module3.pdf` — the official subject / assignment in PDF form.
- `exN/` — exercise folders containing student scripts and implementations.
  - Example: `P3/ex0/ft_command_quest.py` is a tiny CLI exercise script.

## Requirements
- Python 3.8+ (recommended 3.10+)  
- No project-level dependencies declared (no requirements.txt). Individual exercises may rely only on the Python standard library.

## How to run an exercise
1. Clone the repository:
   ```bash
   git clone https://github.com/deep-awak/code-cultivation-poo.git
   cd code-cultivation-poo
   ```

2. Run an example script (replace with the path to the exercise you want):
   ```bash
   python3 P3/ex0/ft_command_quest.py
   ```

3. To run other exercises, open their folder and run the module/script found there:
   ```bash
   python3 P1/ex2/your_script.py
   ```

If an exercise is organized as a package or requires a module import, run it with the `-m` flag from the repository root:
```bash
python3 -m P3.ex0.some_module
```

## Coding standards
- Aim to follow PEP 8 and keep code statically typed where appropriate (type hints).
- Recommended tools you can use locally:
  - Formatting: `black .`
  - Linting: `flake8 .`
  - Static typing: `mypy .`

(These tools are not required by the repo unless you add them — they are suggested to match the project's intent.)

## Resources (exercise subjects)
- P0 subject: `P0/en.subject.pdf`
- P1 subject: `P1/en.subject.pdf`
- P3 subject: `P3/module3.pdf`

Open the corresponding PDF for the full assignment text and verification rules.

## Contributing
This repository is primarily a personal/teaching workspace for exercises. If you want to contribute:
- Fork the repo, implement your exercise, and submit a pull request.
- Keep changes focused (one exercise per PR).
- Include tests or a short README inside the exercise folder if you add non-trivial code.
- Add a LICENSE file if you want to allow reuse.


If you want, I can:
- Commit this README.md into the repo for you (I can create the file and open a PR), or
- Produce a French-localized version, or
- Add a minimal GitHub Actions workflow to run black/flake8/mypy on push. Which would you prefer?
