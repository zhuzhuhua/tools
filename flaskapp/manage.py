# -*- coding: UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from app.hana import hana
# from app._system import _system
# from app.landscape import landscape
import config

app = Flask(__name__)
db = SQLAlchemy(app)
# db.create_all()


app.config.from_object(config)
# app.register_blueprint(hana, url_prefix='/api/hana')
# app.register_blueprint(_system, url_prefix='/api/system')
# app.register_blueprint(landscape, url_prefix='/api/landscape')

if __name__ == '__main__':
    app.run()
