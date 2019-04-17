
from pymongo import MongoClient
from bson import ObjectId 

client = MongoClient("mongodb://localhost:27017") #host uri  
db = client.chatroom  #Select the database  
login = db.auth
notes = db.message
status_posts = db.status_post
friendRequest = db.friend_Requests

notification = db.notifications
chat_history = db.chathistory
   