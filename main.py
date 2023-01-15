from flask import Flask, render_template
from flask_restful import Api

from app.config import Config, db

app = Flask(__name__)

Config.DEBUG = True

app.config.from_object(Config)
db.init_app(app=app)
api = Api(app=app, prefix=Config.API_PREFIX)
app.app_context().push()

from app.views import *

from app.api import PostAPI, PostLikeAPI

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()