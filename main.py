from n_faker import Gen_N
from Executable.exec_01 import execute_sql_file, inner
from Logger.logger_config import log_message
from Database.database import connect_to_database, create_table
  

if __name__ == "__main__":
    # Gen_N(5000)
    # schema = '''
    # CREATE TABLE IF NOT EXISTS CICLINT_ADD (
    #     CICLINT_CLIENT_NUM INTEGER PRIMARY KEY,
    #     CLIENT_NAME TEXT,
    #     CLIENT_EMAIL TEXT,
    #     ACCOUNT_BALANCE REAL,
    #     JOIN_DATE TEXT
    # )
    # '''
    # create_table(connect_to_database('example.db'), schema)
    # auto()
    execute_sql_file('example.db', 'Sql/commands.sql', 'Output\output.xlsx')
    inner('example.db')