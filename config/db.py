from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017")
mydb = conn["Notes"]
mycol = mydb["notes"]

