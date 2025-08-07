# Smart Document Analyzer


## Project Purpose  
Smart Document Analyzer is a Python tool designed to automatically extract text from various document formats, perform natural language processing to identify meaningful entities and summarize content, store the results in a database, and visualize key findings. It helps users quickly gain insights from a large collection of unstructured documents, saving time and enhancing productivity.



## Features  
- Text extraction from PDF, DOCX, TXT, and EML files  
- Named Entity Recognition (NER) using spaCy  
- Text summarization using Hugging Face transformers  
- Storage of entities and summaries in a SQLite database  
- Visualization of entity frequency with bar charts (matplotlib/seaborn)  
- Modular codebase, easy to extend and maintain




## How to Run  
1. **Clone or download the repository**  
2. **Set up Python environment and install dependencies:**  

python -m venv venv
venv\Scripts\activate # For Windows

or
source venv/bin/activate # For macOS/Linux
pip install -r requirements.txt



3. **Place your documents in the `data/` folder**  
4. **Run the full pipeline:**  

cd src
python main.py


This will extract text, perform NLP, store results, and display entity frequency charts.  
5. **(Optional) Run visualization test separately:**  

python test_visualize.py



## Example Output

**Console snippet:**  

Named Entities Detected: [('Apple', 'ORG'), ('U.K.', 'GPE'), ('$1 billion', 'MONEY'), ('Europe', 'LOC')]
Summary: Apple is looking at buying U.K. startup for $1 billion to expand its presence in Europe.

Processed and stored entities for: example.pdf





## Code Documentation  
- All modules contain descriptive docstrings explaining functions, parameters, and return values.  
- In-line comments clarify key logic points for readability and ease of maintenance.

---



![Entity Frequency Bar Chart](output.png)

