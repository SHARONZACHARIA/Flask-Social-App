
from flask import Flask, render_template, jsonify, request,redirect,url_for, request,flash
import json
from flask import session 
from flask import Blueprint
mod = Blueprint('visitor',__name__,template_folder='templates')
from  modules.visitor import checkword as cw
from modules.visitor.cyberbullying import bullymodel
from modules.database import collection 
from modules.chatbot import chatbot as bot
import modules.news as newsdata
import modules.visitor.checkword as cw
import os


import datetime
from werkzeug.utils import secure_filename
from bson.json_util import dumps


 


ALLOWED_EXTENSIONS = set([ 'jpg', 'jpeg'])


@mod.route('/')
def index():
    if session.get('username') !='':
        return redirect(url_for('visitor.userhome'))
    else:
        return render_template('authentication-signin.html')


@mod.route('/user_auth',methods=['POST'])
def userauth():
    uname = request.form.get('uname')
    password = request.form.get('password')
    status= collection.loginuser(uname,password)
    utype=''
    if status.count() ==1:
        for s in status:
            utype= s['utype']
        if utype =='user':
            session['username'] = uname
            session['logged_in'] = True
            return redirect(url_for('visitor.userhome'))

        elif utype =='admin':
            session['username'] = uname
            session['logged_in'] = True
            return redirect(url_for('admin.home'))
       
    else:
        flash("Invalid username or Password")
        return  redirect(url_for('visitor.index'))
    

@mod.route('/userhome')
def userhome():
    if session['logged_in'] == False:
        return "not logged in"
    online_users = collection.FetchOnlineUsers()
    print(online_users)
    return render_template('userhome.html', online = online_users)




@mod.route('/statusUpdates')
def statusUpdates():
    if session['logged_in'] == False:
        return "not logged in"
    status_updates = collection.fetch_all_status()
    return render_template('statusUpdates.html' ,status = status_updates)
       

@mod.route('/update_settings',methods=['POST'])

def update_settings():
    if session['logged_in'] == False:
        return "not logged in"
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    address = request.form.get('address')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    email = request.form.get('email')
    job = request.form.get('job')
    place = request.form.get('address')
    rlshp = request.form.get('relationship')
    personal = request.form.get('personal')
    uname= session['username']
    filename =''
    
    try:
        file = request.files['file']
        if file and file.name != '' and allowed_file(file.filename):
            file.filename = file.filename
            filename = file.filename
            file.save(os.path.join(os.getcwd()+'\\modules\\static\\assets\\uploads\\profile\\',file.filename))
    except:
        print("exception in profile upload")
    print(uname)

    status = collection.add_more(uname,fname,lname,email,phone,address,gender,job,rlshp,personal,place,filename,1)
    flash(status)
    return redirect(url_for('visitor.settings'))




@mod.route('/chat')
def chat():
    if session['logged_in'] == False:
        return "not logged in"
    if session['username'] =='':
        return render_template('authentication-signin.html')
    else:
         #chat_history=collection.fetch_chat(session['username'],touser)
         friends = collection.fetch_friends(session['username'])
         return render_template('chatroom.html', frd = friends)

@mod.route('/chat/<touser>',methods=['GET'])
def chatdata(touser):
    if session['logged_in'] == False:
        return "not logged in"
    if session['username'] =='':
        return render_template('authentication-signin.html')
    else:
         chat_history=collection.fetch_chat(session['username'],touser)
         #friends = collection.fetch_friends(session['username'])
         #print(chat_history)
         return dumps(chat_history)
        

@mod.route('/save_chat/<tuser>/<msg>')
def save_chat(tuser,msg):
    id= collection.save_chat(session['username'],tuser,msg)
    collection.update_seen_message(id,session['username'])
    times= datetimes=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    bully = cw.check_word(msg)
    return jsonify({"msg": msg ,"fuser":session['username'],"times":times,"bully":str(bully)})

@mod.route('/reset')
def reset_password():
    return render_template('authentication-reset-password.html')

@mod.route('/seen/<touser>')
def seen(touser):
    collection.seen(session['username'],touser,session['username'])
    return jsonify({"seen":"yes"})


@mod.route('/recent_chat/<tuser>')
def recent_chat(tuser):
    chat=collection.fetch_chat_recent(session['username'],tuser,session['username'])
    #print(dumps(chat))
    return dumps(chat)

@mod.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@mod.route('/messagebot/<msg>')
def messagebot(msg):
    response=bot.response(msg)
    return jsonify({"message":response})

@mod.route('/logout_user',methods=['GET'])
def logout():
    if collection.lougoutUser(session['username']):
        session['logged_in'] = False
        session['username']=''
        
        return render_template('/authentication-signin.html')
    return 'something went wrong during logout........'

        
   

@mod.route('/show_signup')
def signup():
    return render_template('authentication-signup.html')




@mod.route('/myprofile')

def myprofile():
    if session['logged_in'] == False:
        return "not logged in"
     
    status= collection.retrive_status(session['username'])
    settings = collection.fetch_setting(session['username'])
    return render_template('userprofile.html',status_posts = status, setting = settings)



@mod.route('/signup',methods=['POST'])
def add_user():
    uname = request.form.get('uname')
    password = request.form.get('pass')
    email = request.form.get('email')
    phone = request.form.get('phone')
    lname = request.form.get('lname')
    fname = request.form.get('fname')
    status = collection.auth_user(uname,password,email,phone,fname,lname)
    if status == 1 :
        return render_template('authentication-signin.html')
    flash("Username already exists..")
    return render_template('authentication-signup.html')




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@mod.route('/upload_cover' ,methods=['POST','GET'])

def upload_cover():
     if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
           
            return "someting went wrong 1"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            
            return "something went worng 2" 
        if file and allowed_file(file.filename):
            file.filename = session['username']+".jpg"
            file.save(os.path.join(os.getcwd()+'\\modules\\static\\assets\\uploads\\covers\\',file.filename))
            return redirect(url_for('visitor.myprofile'))


@mod.route('/update_status' , methods=['POST'])
def status():
    uname = request.form.get('uname')
    status = request.form.get('status')
    time= datetime.datetime.now()
    postid = uname+str(time)
    collection.update_status(postid,uname,status,str(time))
    return redirect(url_for('visitor.myprofile'))

@mod.route('/delete_status/<post_id>')
def delete_status(post_id):
    collection.delete_status(post_id)
    return redirect(url_for('visitor.myprofile'))

@mod.route('/searchFriends/<name>')
def searchFriends(name):
    output = dumps(collection.fetchsearch(name))
    return output


@mod.route('/getuserdata')
def getuserdata():
    if session['logged_in']==True:
        data = collection.fetch_setting(session['username'])
        notificationcount = collection.getAllnotificationsCount(session['username'])
        print(session['username'])
    return dumps(data)

@mod.route('/getnoticount')
def getnoticount():
    return jsonify({"count":collection.getAllnotificationsCount(session['username'])})

@mod.route('/sendrequest/<by>/<to>')
def sendrequest(by,to):
    if session['username']=="":
        return url_for('visitor.logout')
    collection.SendFriendRequest(by,to)
    #return jsonify("Friend Request Sent")
    flash("   Freind Request sent ",'info')
    return redirect(url_for('visitor.findf'))

@mod.route('/findf')
def findf():
    if session['logged_in'] == False:
        return "not logged in"
    friendrequestcount = collection.fetch_request_count(session['username'])
    details = collection.fetchDetailsFriendRequests(session['username'])
    return render_template('findf.html',friend = friendrequestcount,detail=details)

@mod.route('/settings')
def settings():
    if session['logged_in'] == False:
        return "not logged in"
    settings = collection.fetch_setting(session['username'])
    return render_template('settings.html' ,setting = settings)

@mod.route('/deletenoti/<id>')
def deletenoti(id):
    collection.deletenotification(id)
    return jsonify({"status":"success"})

@mod.route('/acceptfriend/<frdname>')
def addfriend(frdname):
    collection.AddFriend(session['username'],frdname)
    return redirect(url_for('visitor.findf'))

@mod.route('/rejectfriend/<uname>')
def reject(uname):
    collection.rejectFriend(uname)
    return redirect(url_for('visitor.findf'))

@mod.route('/lost_password',methods=['POST'])
def lost_password():
    if request.method == 'POST':
        mailid = request.json['mailid']
        return collection.lostpassword(mailid)

@mod.route('/notifications/<uname>')
def notifications(uname):
    notifications  = collection.getAllnotifications(uname)
    return render_template('notifications.html',notification = notifications)

@mod.route('/news')
def news():
    news = newsdata.getNews()
    if news =='':
        return render_template('error404.html')
    return render_template('news.html',newsdatas = news)


#implement combo box values to dispaly in settings !!!!!!