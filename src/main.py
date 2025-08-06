import os
from extractors import extract_pdf_text_pypdf2, extract_pdf_text_pdfplumber, extract_docx_text, extract_text_file
from nlp import perform_ner, perform_summarization
from db import connect_db, create_table, insert_record, fetch_entity_frequencies
from visualize import plot_entity_frequencies

# Adjust the DATA_FOLDER path if needed
DATA_FOLDER = '../data'

# Connect to the SQLite database (or create it)
conn = connect_db()
create_table(conn)

# Loop through all files in the data folder
for filename in os.listdir(DATA_FOLDER):
    filepath = os.path.join(DATA_FOLDER, filename)
    text = ""
    try:
        if filename.endswith('.pdf'):
            # You can switch to extract_pdf_text_pdfplumber if preferred
            text = extract_pdf_text_pypdf2(filepath)
        elif filename.endswith('.docx'):
            text = extract_docx_text(filepath)
        elif filename.endswith('.txt') or filename.endswith('.eml'):
            text = extract_text_file(filepath)
        else:
            print(f"Skipping unsupported file: {filename}")
            continue  # Skip unsupported files

        if not text.strip():
            print(f"No text extracted from: {filename}")
            continue  # Skip empty extracts

        entities = perform_ner(text)
        summary = perform_summarization(text)
        for entity_text, entity_label in entities:
            insert_record(conn, filename, entity_text, entity_label, summary)
        print(f"Processed and stored entities for: {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Visualize entity frequency results
df = fetch_entity_frequencies(conn)
if not df.empty:
    plot_entity_frequencies(df)
else:
    print("No entity data available to visualize.")
