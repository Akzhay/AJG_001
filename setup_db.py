# setup_db.py
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///D:/Akay/Pilot01/example.db'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

CICLINT = Table(
    'CICLINT', metadata,
    Column('CICLINT_CLIENT_NUM', Integer, primary_key=True),
    Column('CICLINT_ORG_NAME1', String),
    Column('CICLINT_ORG_NAME2', String)
)

CICLINT_ADD = Table(
    'CICLINT_ADD', metadata,
    Column('CICLINT_CLIENT_NUM', Integer, primary_key=True),
    Column('CLIENT_EMAIL', String),
    Column('ACCOUNT_BALANCE', Integer),
    Column('JOIN_DATE', String)
)

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert sample data
session.execute(CICLINT.insert().values(
    CICLINT_CLIENT_NUM=254110,
    CICLINT_ORG_NAME1='Ramsey Inc',
    CICLINT_ORG_NAME2='Group'
))

session.execute(CICLINT_ADD.insert().values(
    CICLINT_CLIENT_NUM=254110,
    CLIENT_EMAIL='pnewman@example.net',
    ACCOUNT_BALANCE=7120.91,
    JOIN_DATE='2016-03-19'
))

session.commit()
session.close()
