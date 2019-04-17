import json

from flask import Flask
from flask_restful import Api

from resources import Feed, SinglePost, Comments
from models.base import db_session

app = Flask(__name__)
api = Api(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

api.add_resource(Feed, '/feed')
api.add_resource(SinglePost, '/feed/<string:post_id>')
# Routes for Comments
api.add_resource(Comments, '/comments/<int:post_id>')

if __name__ == '__main__':
    app.run(debug=True)
