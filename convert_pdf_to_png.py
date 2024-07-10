import os
from pdf2image import convert_from_path

def pdf_to_png(pdf_path):
    # Get the directory and filename without extension
    dir_name = os.path.dirname(pdf_path)
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)

    # Save images as PNG
    png_path = os.path.join(dir_name, f"{file_name}.png")
    images[0].save(png_path, 'PNG')
    print(f"Saved {png_path}")

if __name__ == "__main__":
    pdf_path = 'us/abdullah_ozer_resume.pdf'
    pdf_to_png(pdf_path)

    pdf_path = 'fr/abdullah_ozer_cv.pdf'
    pdf_to_png(pdf_path)
