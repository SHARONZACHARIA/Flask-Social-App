from flask import Flask

app = Flask(__name__)
UPLOAD_FOLDER = '/static/assets/uploads/covers/'



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.secret_key ='1234'
from modules.visitor.routes import mod
from modules.admin.routes import mod


# register blueprints for api and site

app.register_blueprint(visitor.routes.mod)
app.register_blueprint(admin.routes.mod,url_prefix='/admin')