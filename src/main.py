from db import fetch_entity_frequencies
from visualize import plot_entity_frequencies

conn = connect_db()
df = fetch_entity_frequencies(conn)
plot_entity_frequencies(df)
