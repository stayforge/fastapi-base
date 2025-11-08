# test_db.py
def test_database_connection(test_db):
    """
    Test whether the database can be connected normally.
    """
    assert test_db is not None, "Database object is None"
    assert test_db.ping() == True, "Unable to ping database"
