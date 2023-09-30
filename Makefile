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
	@./.venv/bin/python -m pylint ./source ./config --max-line-length=120 --disable=too-few-public-methods,R0801 --good-names=df,ad,i,n,k

.PHONY: apply_flake8
apply_flake8:
	@./.venv/bin/python -m flake8 ./source ./config --max-line-length=120

.PHONY: apply_mypy
apply_mypy:
	@./.venv/bin/python -m mypy ./source ./config --ignore-missing-import



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


.PHONY: upload_datasets_to_pg  ## Upload title_ratings, title_basics & title_akas to Postgres
upload_datasets_to_pg:
	echo "- Upload title_ratings"
	@./.venv/bin/python ./source/usecase/upload_data_pg.py --dataset=title_ratings
	echo "- Upload title_basics"
	@./.venv/bin/python ./source/usecase/upload_data_pg.py --dataset=title_basics
	echo "- Upload title_akas"
	@./.venv/bin/python ./source/usecase/upload_data_pg.py --dataset=title_akas

.PHONY: upload_datasets_to_ch  ## Upload title_ratings, title_basics & title_akas to Clickhouse
upload_datasets_to_ch:
	@echo "- Upload title_ratings"
	@./.venv/bin/python ./source/usecase/upload_data_ch.py --dataset=title_ratings
	@echo "- Upload title_basics"
	@./.venv/bin/python ./source/usecase/upload_data_ch.py --dataset=title_basics
	@echo "- Upload title_akas"
	@./.venv/bin/python ./source/usecase/upload_data_ch.py --dataset=title_akas