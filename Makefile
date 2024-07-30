.PHONY: install
install:
	poetry install

.PHONY: convert
convert:
	poetry run python convert_pdf_to_png.py
