import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.extractors import (
    extract_pdf_text_pypdf2,
    extract_docx_text,
    extract_text_file,
    extract_html_text,
    extract_excel_text,
    extract_image_text,
)
from src.nlp import perform_ner, perform_summarization

st.set_page_config(page_title="Smart Document Analyzer", layout="wide")
st.title("Smart Document Analyzer ")

# Create data folder to save uploaded files
os.makedirs("data", exist_ok=True)

uploaded_files = st.file_uploader(
    "Upload documents (PDF, DOCX, TXT, EML, HTML, XLSX, PNG/JPG)", accept_multiple_files=True
)

if uploaded_files:
    all_records = []  # In-memory storage of entities + summaries

    for uploaded_file in uploaded_files:
        file_path = os.path.join("data", uploaded_file.name)

        # Save uploaded file
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write(f"Saved: {uploaded_file.name}")

        # Extract text based on file extension
        lower_name = uploaded_file.name.lower()
        if lower_name.endswith(".pdf"):
            text = extract_pdf_text_pypdf2(file_path)
        elif lower_name.endswith(".docx"):
            text = extract_docx_text(file_path)
        elif lower_name.endswith(".txt") or lower_name.endswith(".eml"):
            text = extract_text_file(file_path)
        elif lower_name.endswith(".html") or lower_name.endswith(".htm"):
            text = extract_html_text(file_path)
        elif lower_name.endswith(".xlsx") or lower_name.endswith(".xls"):
            text = extract_excel_text(file_path)
        elif lower_name.endswith((".png", ".jpg", ".jpeg", ".tiff")):
            text = extract_image_text(file_path)
        else:
            st.warning(f"File {uploaded_file.name} is not a supported format. Skipping.")
            continue

        if text and text.strip():
            # Optional: show preview of extracted text for debugging
            st.write(f"Extracted text preview ({uploaded_file.name}):", text[:300])

            # Perform Named Entity Recognition (NER)
            try:
                entities = perform_ner(text)
                if not entities:
                    st.info("No named entities detected.")
            except Exception as e:
                st.error(f"Error during Named Entity Recognition: {e}")
                entities = []

            # Perform Summarization
            try:
                summary = perform_summarization(text)
                if not summary or summary.strip() == "":
                    summary = "Summary not available."
            except Exception as e:
                st.error(f"Error during summarization: {e}")
                summary = "Summary not available."

            # Show summary
            st.subheader(f"Summary for {uploaded_file.name}")
            st.write(summary)

            # Show named entities nicely
            st.subheader(f"Detected Named Entities for {uploaded_file.name}:")
            if entities:
                # Format entities as a DataFrame for better display
                df_entities = pd.DataFrame(entities, columns=["Entity Text", "Entity Label"])
                st.dataframe(df_entities)
            else:
                st.write("No entities detected in this document.")

            # Store entity data + summary for cross-document visualization
            for entity_text, entity_label in entities:
                all_records.append(
                    {
                        "document_name": uploaded_file.name,
                        "entity_text": entity_text,
                        "entity_label": entity_label,
                        "summary": summary,
                    }
                )
        else:
            st.warning(f"No text extracted from {uploaded_file.name}.")

    # Aggregate and visualize entities across all documents uploaded in current session
    if all_records:
        df = pd.DataFrame(all_records)
        freq_df = (
            df.groupby(["entity_text", "entity_label"])
            .size()
            .reset_index(name="frequency")
            .sort_values("frequency", ascending=False)
            .head(20)
        )

        st.subheader("Entity Frequency Chart (Top 20 entities)")

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(
            x="frequency",
            y="entity_text",
            hue="entity_label",
            data=freq_df,
            dodge=False,
            palette="tab10",
            ax=ax,
        )
        ax.set_xlabel("Frequency")
        ax.set_ylabel("Entity")
        ax.set_title("Entity Frequency by Type")
        ax.legend(title="Entity Type", loc="upper right")
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.info("No entities detected yet.")
else:
    st.info("Upload some documents to start analyzing.")
