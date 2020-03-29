SHELL := /bin/bash

MODULE=ekrhizoc
VERSION=$$(poetry version | grep -o [0-9].[0-9].[0-9])

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
	./scripts/helpers/cleanup.sh
