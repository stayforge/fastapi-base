"""

"""
import os

from dotenv import load_dotenv

from src.db.mongodb import MongoDBConnector

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")

tenant_db = MongoDBConnector(uri=mongo_uri, database="tenant")
tenant_collection = tenant_db.get_collection("tenant")
tenant_membership_collection = tenant_db.get_collection("tenant_membership")


apikey_db = MongoDBConnector(uri=mongo_uri, database="apikey")
apikey_collection = apikey_db.get_collection("apikey")