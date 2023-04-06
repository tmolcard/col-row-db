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

.PHONY: local_db_up  ## Create one local Postgres and one local Clickhouse database
local_db_up:
	docker-compose up -d

.PHONY: local_db_stop  ## Stop local databases (Postgres & Clickhouse)
local_db_stop:
	docker-compose stop

.PHONY: local_db_down  ## Drop local databases (Postgres & Clickhouse)
local_db_down:
	docker-compose down
