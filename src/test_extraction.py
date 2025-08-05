from extractors import extract_pdf_text_pdfplumber, extract_docx_text, extract_text_file

# Test PDF extraction
pdf_text = extract_pdf_text_pdfplumber('data/sensors-16-01298.pdf')
print("Extracted PDF text:\n", pdf_text[:500])  # print first 500 chars

# Test DOCX extraction
# Use the actual DOCX file you added
# If the filename contains spaces or special characters, ensure the path is correct

docx_text = extract_docx_text('data/ALP LAB INTERNAL PROGRAMS (1).docx')
print("\nExtracted DOCX text:\n", docx_text[:100000000000000])

# Test plain text extraction (uncomment and set correct path if you have a .txt file)
# text_file_text = extract_text_file('data/sample.txt')
# print("\nExtracted Text File text:\n", text_file_text[:500])
