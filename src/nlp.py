import spacy
from transformers import pipeline

# Load spaCy English model once at the top
nlp = spacy.load('en_core_web_sm')

# Initialize Hugging Face summarization pipeline (model cached on first run)
summarizer = pipeline('summarization')

def perform_ner(text):
    """
    Extract named entities using spaCy.
    Args:
        text (str): Input text to analyze.
    Returns:
        list of tuples: (entity_text, entity_label)
    """
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def perform_summarization(text):
    """
    Summarize text using Hugging Face transformers.
    Truncates input to the first 500 words to fit model limitations.
    
    Args:
        text (str): Input text to summarize.
    Returns:
        str: Summarized text.
    """
    max_input_length = 500
    # Limit length to first 500 words
    input_text = ' '.join(text.strip().split()[:max_input_length])
    summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']
