import config
from flask import Flask,request,render_template
from flask_cors import CORS
from app.controllers.transform import transformCtrl 
from app.controllers.upload import uploadCtrl
from flask_uploads import configure_uploads
from app.modules.upload import upFile


app=Flask(__name__)
CORS(app)
app.config.from_object(config) # 由config.py管理環境變數
configure_uploads(app, upFile)

app.register_blueprint(transformCtrl, url_prefix='/transform')
app.register_blueprint(uploadCtrl, url_prefix='/upload')