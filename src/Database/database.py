
import sqlite3
import logging
from src.Logger.logger_config import log_message
from faker import Faker


def connect_to_database(db_name):
    """
    Connects to the specified SQLite database.
    :param db_name: The name of the database.
    :return: Connection object or None.
    """
    try:
        conn = sqlite3.connect(db_name)
        log_message(f"Successfully connected to database: {db_name}")
        return conn
    except sqlite3.Error as e:
        log_message(f"Error connecting to database: {e}", level=logging.ERROR)
        return None

def create_table(conn,schema):
    """
    Creates a table in the SQLite database.
    :param conn: The Connection object.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(schema)
        conn.commit()
        log_message("Table created successfully.")
    except sqlite3.Error as e:
        log_message(f"Error creating table: {e}", level=logging.ERROR)
        




