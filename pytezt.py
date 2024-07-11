# test_db.py
import pytest
from Database.database import connect_to_database
from unittest.mock import MagicMock, patch

# Define the expected result
expected_result = (254110, 'Ramsey Inc', 'Group', 'pnewman@example.net', 7120.91, '2016-03-19')

connection = connect_to_database('example.db')

# Define the query function (this is a simplified example of what your actual function might look like)
def get_record(connection):
    query = '''
        SELECT a.CICLINT_CLIENT_NUM, 
               a.CICLINT_ORG_NAME1,
               a.CICLINT_ORG_NAME2,
               b.CLIENT_EMAIL, 
               b.ACCOUNT_BALANCE, 
               b.JOIN_DATE
        FROM CICLINT_ADD b
        LEFT JOIN CICLINT a
        ON a.CICLINT_CLIENT_NUM = b.CICLINT_CLIENT_NUM
    '''
    result = connection.execute(query).fetchone()
    return result

# Test function using mocking
def test_record_returned():
    # Create a mock connection object
    mock_connection = MagicMock()

    # Configure the mock to return the expected result
    mock_connection.execute().fetchone.return_value = expected_result

    # Call the function with the mock connection
    result = get_record(mock_connection)

    # Print result and expected for debugging
    print("Result:", result)
    print("Expected:", expected_result)

    # Assert the result matches the expected record
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

if __name__ == '__main__':
    pytest.main(['-s', __file__])
