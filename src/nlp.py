import spacy
from transformers import pipeline

# Load spaCy model (e.g., en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Initialize summarizer from transformers
summarizer = pipeline("summarization")

def perform_ner(text):
    doc = nlp(text)
    # Return list of tuples (entity_text, entity_label)
    return [(ent.text, ent.label_) for ent in doc.ents]

def perform_summarization(text):
    # Handle text longer than max length by truncation or chunking
    try:
        result = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return result[0]['summary_text']
    except Exception as e:
        print(f"Summarization error: {e}")
        return "Summary not available."
