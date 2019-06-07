.PHONY: clean clean-test clean-pyc clean-build clean-docs docs help env
.DEFAULT_GOAL := help

SHELL := /bin/bash
ENV_NAME := bdacore
REPORTS_FOLDER := reports
ENV_PY_VERSION := 3.6.*


define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clean-docs ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -rf .pytest_cache
	rm -f .coverage
	rm -rf reports

clean-docs:
	rm -rf docs/bdacore.*.rst
	rm -rf docs/_build

env: ## create
	conda create -n ${ENV_NAME} python=${ENV_PY_VERSION} -y && \
	source activate ${ENV_NAME} && \
	conda install -y ipykernel && \
	python -m ipykernel install --user --name ${ENV_NAME} --display-name "${ENV_NAME}" && \
	conda clean --all -y

remove: clean
	source activate ${ENV_NAME} && \
	python setup.py clean --all
	source deactivate ${ENV_NAME} && \
	conda remove -y -n "${ENV_NAME}" --all

unittests:
	mkdir -p ${REPORTS_FOLDER}
	source activate ${ENV_NAME} && \
	python setup.py test

develop: ## python setup.py develop equivalent to "pip install -e ."
	source activate ${ENV_NAME} && \
	conda install -y -c conda-forge tensorflow keras seaborn lightgbm nltk && \
	pip install --upgrade pip && \
	pip install -e .[test] && \
	pip install -e . --extra-index-url https://test.pypi.org/simple/

develop_env : env develop

acceptance-tests:
	source activate ${ENV_NAME} && \
	python setup.py test --addopts '-k "functional"'

lint: ## check style with flake8
	flake8 bdacore tests

test-all: unittests acceptance-tests

release: clean ## package and upload a release
	source activate ${ENV_NAME} && \
	python setup.py sdist upload
	python setup.py bdist_wheel upload

package: clean ## builds source and wheel package
	mkdir -p build/linux-64/
	source activate ${ENV_NAME} && \
	python setup.py sdist bdist_wheel

install: clean ## install the package to the active Python's site-packages
	source activate ${ENV_NAME} && \
	python setup.py install
