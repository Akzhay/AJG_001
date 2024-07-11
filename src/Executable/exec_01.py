import csv
import sqlite3
import logging,os
import numpy as np
import pandas as pd
from Logger.logger_config import log_message
from Database.database import connect_to_database



def execute_sql_file(db_name, sql_file, output_file):
    """
    Executes SQL commands from a file and saves the output to a text file.
    :param db_name: The name of the database.
    :param sql_file: The path to the SQL file.
    :param output_file: The path to the output text file.
    """
    # print(db_name, sql_file, output_file,'ak')
    print(os.getcwd())
    try:
        conn = connect_to_database(db_name)
        print('connected')


        with open(sql_file, 'r') as file:
            sql_script = file.read()

        cursor = conn.cursor()
        cursor.execute(sql_script)
        rows = cursor.fetchall()
        
        column_names = [description[0] for description in cursor.description]

        df = pd.DataFrame(rows, columns=column_names)
        df.to_excel(output_file, index=False)

    except sqlite3.Error as e:
        log_message(f"Error executing SQL script: {e}", level=logging.ERROR)
    finally:
        to_tex(column_names, output_file, rows)
        if conn:
            conn.close()
            log_message("Database connection closed.")
            
def to_tex(column_names, output_file, rows):
    output_file = output_file.replace('.xlsx', '.txt')
    try:        
        max_widths = [len(col) for col in column_names]
        for row in rows:
            for i, item in enumerate(row):
                max_widths[i] = max(max_widths[i], len(str(item)))

    # Create a format string with equal space for each column
        format_str = ' '.join([f'{{:<{width}}}' for width in max_widths])

        # Write results to the output text file with formatted space
        with open(output_file, 'w') as file:
            # Write column names
            file.write(format_str.format(*column_names) + '\n')
            file.write(' '.join(['-' * width for width in max_widths]) + '\n')  # Separator line

            # Write each row with formatted space
            for row in rows:
                file.write(format_str.format(*row) + '\n')
    except Exception as e:
        log_message(f"Error executing SQL script: {e}", level=logging.ERROR)
    finally:
        log_message(f"Output saved to: {output_file}")
        
def inner(db_name):
    
    try:
        conn = connect_to_database(db_name)

        cursor = conn.cursor()
        cursor.execute(
                        '''
                        SELECT a.CICLINT_CLIENT_NUM, 
                        a.CICLINT_ORG_NAME1,
                        a.CICLINT_ORG_NAME2,
                        b.CLIENT_EMAIL, 
                        b.ACCOUNT_BALANCE, 
                        b.JOIN_DATE
                        FROM 
                            CICLINT_ADD b
                        LEFT JOIN 
                            CICLINT a
                        ON 
                            a.CICLINT_CLIENT_NUM = b.CICLINT_CLIENT_NUM
                        
                        '''
                    )
        rows = cursor.fetchall()
        
        column_names = [description[0] for description in cursor.description]

        df = pd.DataFrame(rows, columns=column_names)
        df.to_excel('Output\Q_01.xlsx', index=False)

    except sqlite3.Error as e:
        log_message(f"Error executing SQL script: {e}", level=logging.ERROR)
    finally:
        if conn:
            conn.close()
            log_message("Database connection closed.")
    
    
  
