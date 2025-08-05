from db import connect_db, create_table, insert_record, fetch_entity_frequencies

# Assume you have these from extraction/NLP pipeline
doc_name = "sample.pdf"
entities = [("Apple", "ORG"), ("U.K.", "GPE")]
summary = "Apple is acquiring a U.K. startup to expand presence in Europe."

# Save results
conn = connect_db()
create_table(conn)
for entity_text, entity_label in entities:
    insert_record(conn, doc_name, entity_text, entity_label, summary)

# Query the most frequent entities
df = fetch_entity_frequencies(conn)
print(df)
