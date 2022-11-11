docker_run = docker run --rm --mount type=bind,source="$(shell pwd)/",target=/root/ ee-data-engineering-challenge:0.0.1

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build-docker-image
build-docker-image: ## Build the docker image and install python dependencies
	docker build --no-cache -t ee-data-engineering-challenge:0.0.1 .
	$(docker_run) pipenv install --dev

.PHONY: tidy
tidy: ## Tidy code
	$(docker_run) pipenv run tidy

.PHONY: lint
lint: ## Lint the code
	$(docker_run) pipenv run lint

.PHONY: test
test: ## Run tests
	$(docker_run) pipenv run test

.PHONY: fetch-data
fetch-data: ## Fetch the vote data from the remote location
	$(docker_run) pipenv run fetch_data

.PHONY: ingest-data
ingest-data: fetch-data ## Invoke the ingestion process
	$(docker_run) pipenv run python src/ingest.py uncommitted/votes.jsonl

.PHONY: detect-outliers
detect-outliers: ## Invoke the outlier detection process
	$(docker_run) pipenv run python src/outliers.py

.PHONY: run-query
run-query: ## Run an arbitrary query against the database (i.e. make query="select * from posts" run-query)
	$(docker_run) sqlite3 warehouse.db "$(query)"


