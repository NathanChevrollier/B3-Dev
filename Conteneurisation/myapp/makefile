# Variables
PY=python3
PIP=$(PY) -m pip
VENV=.venv
SRC=src/myapp/app.py

# Aide (help) - documentation intégrée dans les commentaires des cibles
help: ### Affiche l'aide des commandes
	@echo "Commandes disponibles :"
	@grep -E '^[a-zA-Z_-]+:.*?###' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS=":.*?###"} {printf "%-10s %s\n", $$1, $$2}'

# Création de l'environnement virtuel si absent
venv: ### Crée l'environnement virtuel .venv
	@test -d $(VENV) || $(PY) -m venv $(VENV)
	@echo "Environnement $(VENV) prêt."

# Installation des dépendances prod + dev
install: venv ### Installe les dépendances (prod + dev)
	$(VENV)/bin/$(PIP) install --upgrade pip
	$(VENV)/bin/$(PIP) install -r requirements.txt
	$(VENV)/bin/$(PIP) install -r requirements-dev.txt

# Exécution de l'application Python
run: venv ### Lance l'application
	$(VENV)/bin/$(PY) $(SRC)

# Lancement des tests pytest en mode silencieux
test: venv ### Lance la suite de tests pytest
	$(VENV)/bin/$(PY) -m pytest -q

# Analyse statique du code avec ruff
lint: venv ### Analyse statique avec ruff
	$(VENV)/bin/ruff check src tests

# Formatage du code avec black
format: venv ### Formate le code avec black
	$(VENV)/bin/black src tests

# Combinaison lint + test
check: lint test ### Lint + tests combinés

# Nettoyage des artefacts Python (pyc, cache...) et dossiers de build
clean: ### Nettoie artefacts (pyc, __pycache__)
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	rm -rf .pytest_cache build dist *.egg-info

# Nettoyage complet + suppression de l'environnement virtuel
distclean: clean ### Nettoie + supprime .venv et dossiers de build
	rm -rf $(VENV)

# Création du package source + wheel (sdist + wheel)
package: venv ### Construit la distribution (sdist/wheel)
	$(VENV)/bin/$(PY) -m build

# Déclaration des cibles « non-fichiers »
.PHONY: help venv install run test lint format check clean distclean package
