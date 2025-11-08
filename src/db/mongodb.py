import logging

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
logger = logging.getLogger(__name__)


class MongoDBConnector:
    """
    A basic MongoDB connector class to handle the connection for MongoDB Atlas.
    Supports context management to automatically close connections.
    """

    def __init__(self, uri: str, database: str):
        """
        Initialize the MongoDBConnector with a MongoDB Atlas URI and database name.
        :param uri: MongoDB connection URI (e.g., "mongodb+srv://<username>:<password>@cluster.mongodb.net")
        :param database: Name of the database to connect to
        """
        self.uri = uri
        self.database_name = database

        try:
            self.client = MongoClient(self.uri, server_api=ServerApi('1'))
            self.db = self.client[self.database_name]
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {e}")

    def ping(self):
        """
        Ping the MongoDB server and verify the connection.
        Returns True if successful, otherwise raises an exception.
        """
        if not self.client:
            raise ConnectionError("MongoDB client is not initialized")
        try:
            response = self.client.admin.command('ping')
            return response.get('ok', 0) == 1  # Return True if 'ok': 1
        except Exception as e:
            raise ConnectionError(f"Failed to ping MongoDB: {e}")

    def disconnect(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            self.client = None
            print("Disconnected from MongoDB Atlas")

    def get_collection(self, collection_name: str):
        """
        Get a collection object from the database.
        :param collection_name: Name of the collection
        :return: Collection object
        """
        if self.db is None:
            raise ConnectionError("MongoDB database is not initialized")
        return self.db[collection_name]
