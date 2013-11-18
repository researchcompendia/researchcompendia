.PHONY: clean-pyc clean-build docs

help:
	@echo "clean - remove artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with django nose"
	@echo "docs - generate Sphinx HTML documentation, including API docs"

clean: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 companionpages

test: lint
	companionpages/manage.py test --traceback --debug=DEBUG

docs:
	rm -f docs/companionpages.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ companionpages
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html
