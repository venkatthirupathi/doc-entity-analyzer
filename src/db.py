import sqlite3

def connect_db(db_name="smart_doc_analyzer.db"):
    """
    Connect to SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    """
    Create a table to store extracted document info if it doesn't exist.
    """
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS document_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_name TEXT,
            entity_text TEXT,
            entity_label TEXT,
            summary TEXT
        );
    ''')
    conn.commit()

def insert_record(conn, document_name, entity_text, entity_label, summary):
    """
    Insert one record of entities and summary into the database.
    """
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO document_info (document_name, entity_text, entity_label, summary) VALUES (?, ?, ?, ?)',
        (document_name, entity_text, entity_label, summary)
    )
    conn.commit()

def fetch_entity_frequencies(conn):
    """
    Query entity frequencies grouped by entity text and label.
    Returns a pandas DataFrame.
    """
    import pandas as pd
    query = '''
        SELECT entity_text, entity_label, COUNT(*) as frequency
        FROM document_info
        GROUP BY entity_text, entity_label
        ORDER BY frequency DESC
    '''
    return pd.read_sql_query(query, conn)
