import os
from dotenv import load_dotenv
from pymongo import MongoClient

conn = MongoClient(os.getenv("DB_URL"))