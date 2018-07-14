.PHONY: deploy
deploy: dev-dependencies
	chalice deploy --profile sandbox

.PHONY: dev-dependencies
dev-dependencies:
	pip install -r requirements.txt
