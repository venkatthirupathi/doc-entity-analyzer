# import matplotlib.pyplot as plt
# import seaborn as sns

# def plot_entity_frequencies(df):
#     """
#     Plot a horizontal bar chart showing the frequency of named entities by type.
#     Args:
#         df (pandas.DataFrame): DataFrame with columns 'entity_text', 'entity_label', 'frequency'
#     """
#     plt.figure(figsize=(10, 6))
#     sns.barplot(
#         x='frequency',
#         y='entity_text',
#         hue='entity_label',
#         data=df,
#         dodge=False
#     )
#     plt.title('Entity Frequency by Type')
#     plt.xlabel('Frequency')
#     plt.ylabel('Entity')
#     plt.legend(title='Entity Type')
#     plt.tight_layout()
#     plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

def plot_entity_frequencies(df, top_n=20):
    """
    Plot a horizontal bar chart for the top N most frequent named entities.
    Args:
        df (pandas.DataFrame): columns ['entity_text', 'entity_label', 'frequency']
        top_n (int): show only the top N entities
    """
    # Sort and select the top entities
    df = df.sort_values('frequency', ascending=False).head(top_n)
    plt.figure(figsize=(12, max(6, top_n // 2)))  # larger size if N is high

    sns.barplot(
        x='frequency',
        y='entity_text',
        hue='entity_label',
        data=df,
        dodge=False
    )
    plt.title(f'Entity Frequency by Type (Top {top_n})')
    plt.xlabel('Frequency')
    plt.ylabel('Entity')
    plt.legend(title='Entity Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.yticks(fontsize=8)
    plt.tight_layout()

    plt.savefig("output.png")   # Save the current figure as an image
# plt.show()                 # Then display the chart

    plt.show()
