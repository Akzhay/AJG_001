import sqlite3
from src.Database.database import connect_to_database

def list_tables(db_path):
    """Lists the tables in the specified SQLite database."""
    # Connect to the SQLite database
    conn = connect_to_database('example.db')
    cursor = conn.cursor()
    
    # Execute the query to get the list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    # Extract table names from the query result
    table_names = [table[0] for table in tables]
    return table_names

# Example usage
db_path = 'example.db'
print("Tables in the database:", list_tables(db_path))