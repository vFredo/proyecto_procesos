from pymongo import MongoClient
from app.api.config.env import MONGO_CLIENT

conn = MongoClient(MONGO_CLIENT)
