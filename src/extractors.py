import os
from bs4 import BeautifulSoup
import pandas as pd
from PIL import Image
import pytesseract

from PyPDF2 import PdfReader
import docx

def extract_pdf_text_pypdf2(path):
    text = ""
    try:
        reader = PdfReader(path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"PDF extraction error for {path}: {e}")
    return text.strip()

def extract_docx_text(path):
    text = ""
    try:
        doc = docx.Document(path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"DOCX extraction error for {path}: {e}")
    return text.strip()

def extract_text_file(path):
    text = ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Text file extraction error for {path}: {e}")
    return text.strip()

def extract_html_text(path):
    text = ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            text = soup.get_text(separator=" ")
    except Exception as e:
        print(f"HTML extraction error for {path}: {e}")
    return text.strip()

def extract_excel_text(path):
    text = ""
    try:
        df = pd.read_excel(path, dtype=str).fillna("")
        # Join all cell texts row-wise and then combine rows
        text = "\n".join(df.astype(str).apply(" ".join, axis=1))
    except Exception as e:
        print(f"Excel extraction error for {path}: {e}")
    return text.strip()

def extract_image_text(path):
    text = ""
    try:
        image = Image.open(path)
        text = pytesseract.image_to_string(image)
    except Exception as e:
        print(f"OCR extraction error for {path}: {e}")
    return text.strip()
