install:
	poetry install

convert:
	poetry run python convert_pdf_to_png.py
