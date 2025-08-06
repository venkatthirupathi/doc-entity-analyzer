# src/test_visualize.py

import pandas as pd
from visualize import plot_entity_frequencies

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))
# from visualize import plot_entity_frequencies
# from visualize import plot_entity_frequencies
from visualize import plot_entity_frequencies



# Example DataFrame, replace this with result from your database
data = {
    'entity_text': ['Apple', 'U.K.', 'Microsoft', 'London', 'Google'],
    'entity_label': ['ORG', 'GPE', 'ORG', 'GPE', 'ORG'],
    'frequency': [10, 7, 5, 3, 2]
}
df = pd.DataFrame(data)

# Plot the entity frequencies
# plot_entity_frequencies(df)
plot_entity_frequencies(df, top_n=20)


# f = <your DataFrame from database or sample>

# Now, just call with top_n:
plot_entity_frequencies(df, top_n=20)  # Shows only top 20 entities
