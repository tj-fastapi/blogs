.PHONY: run
run:
	@cd app && uvicorn main:app --reload

.PHONY: install
install:
	@pip install -r app/requirements.txt

.PHONY: deploy
deploy:
	@cd app && deta deploy
