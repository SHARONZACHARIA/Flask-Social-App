import os
from modules.database import dataconnect as cn
import datetime
from flask import session
from modules.visitor import checkword as cw


def getAllOffensivePosts():
    return cn.status_posts.find({
        "bully_status":"[1]"
    })

def getMail(uname):
    return cn.login.find({"uname":uname},{"email":1})

def blockUser(uname):
    cn.login.update_one({"uname":uname},{"$set":{"allowed":"no"}})

def delete_post(postid):
    cn.status_posts.delete_one({"post_id":postid})

def blocked_users():
    return cn.login.find({"allowed":"no"},{"uname":1,"fname":1,"lname":1,"email":1,"phone":1})

def unblock(uname):
    cn.login.update_one({"uname":uname},{"$set":{"allowed":"yes"}})
    
