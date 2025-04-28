from flask import Flask
from public import public
from admin import admin
from psychiatrist import psychiatrist
from meditation import meditation
from api import apiss
from user import user
# from chatbot import chatb

app=Flask(__name__)

app.secret_key="ddd"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(meditation)
app.register_blueprint(psychiatrist)
app.register_blueprint(user)
# app.register_blueprint(chatb)
app.register_blueprint(apiss,url_prefix='/api')

app.run(debug=True,port=5990
        
        
        
         ,host="0.0.0.0")