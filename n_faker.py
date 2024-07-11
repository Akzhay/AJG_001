import random
import sqlite3
from faker import Faker
from Logger.logger_config import log_message
from Database.database import connect_to_database

# Initialize Faker
fake = Faker()

# Connect to SQLite database (or create it if it doesn't exist)
conn = connect_to_database('example.db')
cursor = conn.cursor()

# Function to generate a single record
def generate_record():
    return (
        fake.iso8601(),
        random.choice(['A1', 'B2', 'C3']),
        fake.date(),
        fake.unique.random_number(digits=6, fix_len=True),
        fake.company(),
        fake.company_suffix(),
        fake.street_address(),
        fake.secondary_address(),
        fake.street_name(),
        fake.city(),
        fake.state_abbr(),
        fake.country_code(),
        fake.zipcode(),
        fake.word(),
        random.choice(['SSN', 'EIN']),
        fake.ssn(),
        fake.phone_number(),
        fake.phone_number(),
        fake.phone_number()
    )

# Generate and insert 5000 records
def Gen_N(hmany):
    records = [generate_record() for _ in range(hmany)]
    cursor.executemany('''
    INSERT INTO CICLINT (
        CICLINT_TSTAMP, CICLINT_STATUS_CODE, CICLINT_STATUS_DATE, CICLINT_CLIENT_NUM,
        CICLINT_ORG_NAME1, CICLINT_ORG_NAME2, CICLINT_ADDRESS1, CICLINT_ADDRESS2,
        CICLINT_ADDRESS3, CICLINT_CITY, CICLINT_STATE, CICLINT_CNTRY_CODE,
        CICLINT_POSTAL_CODE, CICLINT_NAME_SORT, CICLINT_TAX_ID_TYPE, CICLINT_TAX_ID,
        CICLINT_PHONE, CICLINT_TELEX, CICLINT_FAX
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', records)

    # Commit and close connection
    conn.commit()
    conn.close()
    print(f'done inserting using faker')
    log_message(f"{hmany} records inserted successfully.")
