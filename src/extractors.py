import PyPDF2
import pdfplumber
import docx

def extract_pdf_text_pypdf2(filepath):
    """
    Extract text from a PDF file using PyPDF2.
    Returns extracted text as a single string.
    """
    text = []
    try:
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return '\n'.join(text)
    except Exception as e:
        print(f"Error extracting PDF with PyPDF2: {e}")
        return ""

def extract_pdf_text_pdfplumber(filepath):
    """
    Extract text from a PDF file using pdfplumber.
    Returns extracted text as a single string.
    """
    text = []
    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return '\n'.join(text)
    except Exception as e:
        print(f"Error extracting PDF with pdfplumber: {e}")
        return ""

def extract_docx_text(filepath):
    """
    Extract text from a DOCX (Word) document.
    Returns extracted text as a single string.
    """
    try:
        doc = docx.Document(filepath)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)
        return '\n'.join(text)
    except Exception as e:
        print(f"Error extracting DOCX: {e}")
        return ""

def extract_text_file(filepath):
    """
    Extract text from a plain text or email (.eml) file.
    Returns the file content as a string.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error extracting text file: {e}")
        return ""
