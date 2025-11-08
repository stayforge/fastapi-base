# conftest.py
import os

import pytest
from dotenv import load_dotenv

from src.db.mongodb import MongoDBConnector

load_dotenv()


@pytest.fixture(scope="session")
def mongodb_uri():
    """
    Get the MongoDB connection URI and make sure it is set correctly.
    """
    mongodb_uri = os.environ.get("MONGODB_URI")
    if not mongodb_uri:
        raise ValueError("Environment variable 'MONGODB_URI' is not set or empty.")
    return mongodb_uri


@pytest.fixture(scope="function", autouse=True)
def test_db(mongodb_uri):
    """
    Initialize and provide the Database object, and ensure collections are cleared before and after each test.
    """
    db = MongoDBConnector(uri=os.getenv("MONGODB_URI"), database="api_analytics")
    did_ping = db.ping()
    assert did_ping is True, "Failed to connect to MongoDB"
    yield db

    collections = db.client.db.list_collection_names()
    for collection in collections:
        db.client.db[collection].delete_many({})

    db.disconnect()
