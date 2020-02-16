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

### Util ###
.PHONY : clean
clean :
	./scripts/helpers/conda-remove-env.sh