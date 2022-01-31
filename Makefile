
DETA_DIR  := ./app/.deta

.PHONY: run
run:
	@cd app && uvicorn main:app --reload

.PHONY: install
install:
	@pip install -r app/requirements.txt

.PHONY: deploy
deploy:
ifneq "$(wildcard $(DETA_DIR) )" ""
	@echo "Found deta micro"
	@echo "Updating existing deta micro..."
	@cd app && deta deploy
else
	@echo "Did not find deta micro."
	@echo "Creating a new deta micro..."
	@cd app && deta new
endif
