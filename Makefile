PYTHON ?= python3

.PHONY: check sync-base

check:
	$(PYTHON) -m unittest discover -s tests -v
	$(PYTHON) scripts/sync_base.py

sync-base:
	$(PYTHON) scripts/sync_base.py --write
