from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class MongoDBHandler:
    def __init__(self):
        # Setup MongoDB connection
        self.uri = os.getenv('MONGO_CONNECTION_STRING')
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client['pdf']
        self.collection = self.db.sample_pdf

    def insert_data(self, pages_data):
        """
        Inserts parsed data into the MongoDB collection.
        
        :param pages_data: A list of dictionaries, each representing parsed data from a PDF page.
        """
        if pages_data:
            self.collection.insert_many(pages_data)
