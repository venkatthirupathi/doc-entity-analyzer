import matplotlib.pyplot as plt
import seaborn as sns

def plot_entity_frequencies(df):
    """
    Plot a horizontal bar chart showing the frequency of named entities by type.
    Args:
        df (pandas.DataFrame): DataFrame with columns 'entity_text', 'entity_label', 'frequency'
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x='frequency',
        y='entity_text',
        hue='entity_label',
        data=df,
        dodge=False
    )
    plt.title('Entity Frequency by Type')
    plt.xlabel('Frequency')
    plt.ylabel('Entity')
    plt.legend(title='Entity Type')
    plt.tight_layout()
    plt.show()
