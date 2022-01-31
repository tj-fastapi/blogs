.PHONY: run
run:
	cd app && uvicorn main:app --reload