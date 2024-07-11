from faker import Faker
import random
import sqlite3

# Initialize the Faker generator
faker = Faker()

# List of primary keys
primary_keys = [
    853839, 814810, 118101, 260480, 717461, 272297, 774531, 764032, 791584, 831748, 
    905572, 608131, 308550, 846301, 254110, 991575, 502160, 336430, 852762
]

# Function to generate SQL insert statements and execute them using SQLite3
def insert_ciclient_records(primary_keys, db_file):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Generate and execute SQL insert statements
        for client_num in primary_keys:
            name = faker.name()
            email = faker.email()
            account_balance = round(random.uniform(100.0, 10000.0), 2)
            join_date = faker.date_between(start_date='-20y', end_date='today').strftime("%Y-%m-%d")

            # Prepare the SQL insert statement
            sql_insert = f"INSERT INTO CICLINT_ADD (CICLINT_CLIENT_NUM, CLIENT_NAME, CLIENT_EMAIL, ACCOUNT_BALANCE, JOIN_DATE) " \
                         f"VALUES (?, ?, ?, ?, ?)"

            # Execute the SQL insert statement with parameters
            cursor.execute(sql_insert, (client_num, name, email, account_balance, join_date))
            print(f"Inserted record for client number {client_num}")

        # Commit the transaction
        conn.commit()
        print("Records inserted successfully into CICLINT_ADD table")

    except sqlite3.Error as e:
        print(f"Error inserting records into CICLINT_ADD table: {e}")

    finally:
        # Close the database connection
        if conn:
            conn.close()

# Example usage:
db_file = 'example.db'  # Replace with your SQLite database file path
insert_ciclient_records(primary_keys, db_file)
