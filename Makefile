SHELL := /bin/bash
.SHELLFLAGS = -ec
.ONESHELL:
.SILENT:

.EXPORT_ALL_VARIABLES:
REPO_DIRECTORY:=$(shell pwd)
PYTHONPATH:=${PYTHONPATH}:${REPO_DIRECTORY}

.PHONY: help
help:
	echo "❓ Use \`make <target>'"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'


.PHONY: apply_pylint
apply_pylint:
	@./.venv/bin/python -m pylint ./data_manipulation --max-line-length=120

.PHONY: apply_flake8
apply_flake8:
	@./.venv/bin/python -m flake8 ./data_manipulation

.PHONY: apply_mypy
apply_mypy:
	@./.venv/bin/python -m mypy ./data_manipulation --ignore-missing-import



.PHONY: apply_linters  ## Apply linters on python codebase
apply_linters: apply_pylint apply_flake8 apply_mypy

.PHONY: local_db_up  ## Create one local Postgres and one local Clickhouse database
local_db_up:
	docker-compose up -d

.PHONY: local_db_stop  ## Stop local databases (Postgres & Clickhouse)
local_db_stop:
	docker-compose stop

.PHONY: local_db_down  ## Drop local databases (Postgres & Clickhouse)
local_db_down:
	docker-compose down

