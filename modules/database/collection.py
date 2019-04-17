import os
from modules.database import dataconnect as cn
import datetime
from flask import session,jsonify
from modules.visitor import checkword as cw
from modules.admin.Mails import sendmail
from bson.objectid import ObjectId


def loginuser(uname,password):
     t= cn.login.find({"uname":uname,"password":password,"allowed":"yes"})
     if t.count() > 0 :
        cn.login.update_one({"uname":uname},{'$set':{'login_status':1}})
        return t
            
     else:
        return t
     cn.client.close()


def auth_user(uname,password,email,phone,fname,lname):
    t= cn.login.find({"uname":uname}).count()
    if t > 0 :
                
        return 0 #username alredy exists 
    else:
        print(cn.login.find())
        id = cn.login.insert_one({"uname":uname,"password":password,"email":email,"login_status":0 ,
        "fname":fname,"lname":lname,"filename":"default.jpg","allowed":"yes","phone":phone,"place":"","personal":"","relationship":"",
        "job":"","gender":"","address":"","friends":[],"utype":"user"})
        print(id)
    if id is not None:
        return 1  #added
    else:
        return  "somethig went wrong " #unsucessfull
    cn.client.close()
    

def lostpassword(email):
    userPassword = cn.login.find({"email":email},{"password":1})
    title ="Password Reset"
    userPass=''
    for d in userPassword:
        userPass = d['password']
    if userPass =='':
        return jsonify({"status":"failure"})
    body="your password is "+userPass
    #print("password:"+ userPass)
    receiver= email
    return sendmail(title,body,receiver)



def FetchOnlineUsers():    # fetchallfriends
    array = cn.login.find({"uname":session['username']},{"friends":1})
    for a in array:    
        data=(cn.login.find({
        "uname":{
            "$in":a['friends']
        }
        }))
    return data   


    

def lougoutUser(name):
    cn.login.update_one({"uname":name},{'$set':{'login_status':0}})
    return 1

def update_status(postid,uname,status,time):
    bully_status = str(cw.check_word(status))
    propic = cn.login.find_one({"uname":uname},{"filename":1})
    print(propic)
    pro = propic['filename']
    cn.status_posts.insert_one({'postid':postid,'uname':uname,'status':status,'time':time,'bully_status':bully_status,"propic":pro})
    datetimes=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    addnotification(uname,"You have updated the status post",datetimes)
    return 1

def retrive_status(uname):
    return cn.status_posts.find({'uname':uname})

def delete_status(post_id):
    cn.status_posts.delete_one({'postid':post_id})

def get_propic(uname):
    propic = cn.login.find({"uname":uname},{"filename":1})
    return propic


def add_more(uname,fname,lname,email,phone,address,gender,job,rlshp,personal,place,filename,logstat):
    existing_count = cn.login.find({"uname":uname}).count()
    existing_details = cn.login.find_one({"uname":uname})
    if filename =='':
        filename = existing_details['filename']
    if existing_count > 0 :
         cn.login.update_one({"uname":uname},{'$set':{"fname":fname,"lname":lname ,"email":email,"phone":phone,
         "address":address,"gender":gender,"job":job,"relationship":rlshp,"personal":personal,"place":place,"filename":filename}})
         cn.status_posts.update({"uname":uname},{"$set":{"propic":filename}})
         return "updated"
    else :
         cn.login.insert_one({"uname":uname,"fname":fname,"lname":lname ,"email":email,"phone":phone,
         "address":address,"gender":gender,"job":job,"relationship":rlshp,"personal":personal,"place":place,"filename":filename})
         cn.status_posts.update({"uname":uname},{"$set":{"propic":filename}})
         return "new data"
    
def fetch_setting(name):
    return cn.login.find_one({"uname":name},{"password":0})

def fetch_all_status():
     return cn.status_posts.find()

def fetchsearch(name):
    #array = cn.login.find({"uname":session['username']},{"friends":1})
    #or a in array:    
      #  data = cn.login.find({"$and":[{"uname":{"$regex":name}},{"uname":{"$nin":a['friends']}]})
    #return data  
    array = cn.login.find({"uname":session['username']},{"friends":1}).distinct("friends")
    return cn.login.find({"$and":[{"uname":{"$regex":name}},{"uname":{"$nin":array}},{"utype":"user"}]})  




#friends

def SendFriendRequest(by,to):
    cn.friendRequest.insert({"from":by,"to":to})
    datetimes=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    addnotification(to,"You have a frien request from "+by,datetimes)

def fetch_request_count(name):
    return cn.friendRequest.find({"to":name}).count()

def AddFriend(uname,frdname):
    cn.login.update({"uname":uname},{"$push":{"friends":frdname}})
    cn.login.update({"uname":frdname},{"$push":{"friends":uname}})
    cn.friendRequest.delete_one({"from":frdname,"to":uname})

def rejectFriend(uname):
    cn.friendRequest.remove({"from":uname,"to":session['username']})




   

def fetchDetailsFriendRequests(uname):
    
    array = cn.friendRequest.find({"to":uname},{"from":1,"_id":0}).distinct("from")  
    data=(cn.login.find({
        "uname":{
            "$in":array
        }
    }))
    return data  
  

def fetch_friends(uname):
    array = cn.login.find({"uname":uname},{"friends":1})
    for a in array:    
        data=(cn.login.find({
        "uname":{
            "$in":a['friends']
        }
        }))
    return data    






#chat


def save_chat(fuser,tuser,msg):
    bully = cw.check_word(msg)
    datetimes=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    chat_id = ''.join(sorted(fuser+tuser))
    id = cn.chat_history.insert({
        "chat_id":chat_id,
        "fuser":fuser,
        "tuser":tuser,
        "msg":msg,
        "seen":[""],
        "times":datetimes,
        "bully":str(bully)

    })
    return id

def fetch_chat(fuser,tuser):                                             #fetching all chat of a chatroom
        return cn.chat_history.find({
           "chat_id": ''.join(sorted(fuser+tuser))
        })

def fetch_chat_recent(fuser,tuser,user):                        #fetching recent chat of a chatroom that a user has not seen 
        return cn.chat_history.find({
           "chat_id": ''.join(sorted(fuser+tuser)),"seen":{"$nin":[user]}
        })
    
def update_seen_message(id,user):
    cn.chat_history.update({
        "_id":id},{"$push":{"seen":user}}
    )


def seen(fuser,tuser,user):
    chat_id = ''.join(sorted(fuser+tuser))
    cn.chat_history.update_many({"chat_id":chat_id,"seen":{"$nin":[user]}},{"$push":{"seen":user}})



#Notifications

def addnotification(uname,notification,time):
    cn.notification.insert({"uname":uname,"info":notification,"time":time})
    
def getAllnotifications(uname):
    return cn.notification.find({"uname":uname})
    

def deletenotification(id):
    print(id)
    cn.notification.delete_one({"_id":ObjectId(id)})

def getAllnotificationsCount(uname):
    return cn.notification.find({"uname":uname}).count()



    
    
