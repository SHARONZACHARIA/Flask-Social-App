from flask import Flask, render_template, jsonify, request,redirect,url_for, request,json
from flask import session 
from flask import Blueprint
from modules.admin import Mails
from bson.json_util import dumps
import os
import datetime
from modules.database import collection
from modules.database import adminoperations as adminop
mod = Blueprint('admin',__name__,template_folder='templates')


@mod.route('/home')
def home():
    if  session['logged_in']== False:
        return redirect(url_for('visitor.index'))
    bully_data = adminop.getAllOffensivePosts()
    return render_template("bullydata.html",data=bully_data)

@mod.route('/sendmail/<title>/<body>/<receiver>')
def sendmail(title,body,receiver):
    return Mails.sendmail(title,body,receiver)

@mod.route('/getmail/<user>')
def getmail(user):
    return dumps(adminop.getMail(user))

@mod.route('/blockuser',methods=['POST'])
def blockuser():
    adminop.blockUser(request.json['uname'])
    return jsonify({"status":"success"})

@mod.route('/deletepost')
def deletepost(postid):
    adminop.delete_post(postid)
    
    return jsonify({"status":"success"})

@mod.route('/blockedusers')
def blockedusers():
    if session['logged_in'] == False:
        return redirect(url_for('visitor.index'))
    blocked_users = adminop.blocked_users()
    print(blocked_users)
    return render_template('blockedusers.html', blocked_users = blocked_users)

@mod.route('/unblock',methods=['POST'])
def unblock():
    adminop.unblock(request.json['uname'])
    return jsonify({"status":"success"})

@mod.route('/train')
def train():
    return render_template('train.html')

@mod.route('/admin_chatbot')
def admin_Chatbot():
    if  session['logged_in'] ==False :
        return redirect(url_for('visitor.index'))
    return render_template('admin_chatbot.html')

@mod.route('/update_chatbot/<content>')
def update_chatbot(content):
    filepath = os.getcwd()
    f = open(filepath+'/modules/chatbot/chatbot.txt',"a")
    f.write(content)
    f.close()
    datetimes=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    collection.addnotification("all","contents of chatbot have been updated",datetimes)
    return jsonify({"status":"success"})
    
