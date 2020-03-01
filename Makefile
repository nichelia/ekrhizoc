SHELL := /bin/bash

MODULE=ekrhizoc
VERSION=$$(poetry version | grep -o [0-9].[0-9].[0-9])

EKRHIZOC_WHEEL=$$(find . -type f -name "*.whl")
EKRHIZOC_WHEEL_NAME=$$(basename $(EKRHIZOC_WHEEL))

### Environment ###
.PHONY: env
env:
	./scripts/helpers/environment.sh

.PHONY: env-prod
env-prod:
	./scripts/helpers/environment.sh -p

.PHONY: env-update
env-update:
	./scripts/helpers/environment.sh -f

### Git ###
.PHONY: git-hooks
git-hooks:
	chmod +x githooks/*
	mkdir -p .git/hooks
	cd .git/hooks && ln -sf ../../githooks/* .

### PIP ###
.PHONY: build-package
build-package:
	poetry build

.PHONY: publish-package
publish-package:
	poetry publish

### Docker ###
.PHONY: build-docker
build-docker:
	./scripts/build_docker_image.sh

### Test ###
.PHONY: test
test:
	pytest -v

.PHONY: test-coverage
test-coverage:
	pytest --cov=. --cov-report=term-missing

### Util ###
.PHONY : clean
clean :
	./scripts/helpers/conda-remove-env.sh
	rm -rf bin dist .pytest_cache .coverage *.egg-info *.log
	find . -path "*/__pycache__" -type d -exec rm -r {} ';'