from pymongo import MongoClient
from datetime import datetime

client = MongoClient("YOUR_MONGODB_CONNECTION_URI")
db = client.senkron

async def store_message(data):
    db.messages.insert_one({**data, "timestamp": datetime.utcnow()})

async def store_reply(user_id, reply):
    db.replies.insert_one({"user_id": user_id, "reply": reply, "timestamp": datetime.utcnow()})
