import pytest
from sqlalchemy import create_engine, text

@pytest.fixture
def db_connection():
    engine = create_engine('sqlite:///:memory:')
    connection = engine.connect()
    yield connection
    connection.close()

def test_db_connection(db_connection):
    result = db_connection.execute(text('SELECT 1'))
    assert result.fetchone()[0] == 1