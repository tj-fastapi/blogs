# Self-Documented Makefile see https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.DEFAULT_GOAL := help

DETA_DIR  := ./app/.deta

# Put it first so that "make" without argument is like "make help".
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-32s-\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: run
run:  ## Run the blog application using uvicorn
	@cd app && uvicorn main:app --reload

.PHONY: install
install:  ## Install application dependencies
	@pip install -r app/requirements.txt

.PHONY: deploy
deploy:  ## Deploy the application to deta.sh
ifneq "$(wildcard $(DETA_DIR) )" ""
	@echo "Found deta micro"
	@echo "Updating existing deta micro..."
	@cd app && deta deploy
else
	@echo "Did not find deta micro."
	@echo "Creating a new deta micro..."
	@cd app && deta new
endif
