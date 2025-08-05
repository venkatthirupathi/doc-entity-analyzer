from nlp import perform_ner, perform_summarization

sample_text = "Apple is looking at buying U.K. startup for $1 billion. The acquisition will help Apple expand its presence in Europe."

print("Named Entities:", perform_ner(sample_text))
print("\nSummary:", perform_summarization(sample_text))
