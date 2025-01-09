
# source .venv/bin/activate

.PHONY: run
run:
	uv run scripts/run.py

.PHONY: clear
clear:
	uv run scripts/clear.py
