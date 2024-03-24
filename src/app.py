"""
Basic functionality based on: https://github.com/TrevorChan1/EC530-flaskrestful-demo/tree/main/3.%20demo_with_database

Other references:
https://medium.com/@dennisivy/my-first-crud-app-with-fast-api-74ac190d2dcc
https://medium.com/@dennisivy/flask-restful-crud-api-c13c7d82c6e5
https://stackoverflow.com/questions/73961938/flask-sqlalchemy-db-create-all-raises-runtimeerror-working-outside-of-applicat
"""

from flask import Flask, jsonify, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)

# Connect to local 'database.db' SQLite file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')
db = SQLAlchemy(app)

''' Standard SQL Commands
(https://www.freecodecamp.org/news/basic-sql-commands/)
CREATE TABLE users (id INT PRIMARY KEY, name TEXT NOT NULL);  -- Create new table
SELECT name FROM users WHERE id = 1;  -- Retrieve filtered data; DELETE to del record instead
ALTER TABLE main.users DROP COLUMN secret;  -- Delete a column from a table; ADD to add col instead
'''

'''cURL Command Examples
curl -H "Content-Type: application/json" -d '{"name":"foo"}' http://localhost:8000/user/3
# (failed) curl http://localhost:8000/user -d "name=foo" -X PUT
'''


# Define SQLite table schema
class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, id, name):
        self.id   = id
        self.name = name

    def __repr__(self):
        return self.name


# Define output data schema
user_definition = {
    'user_id': fields.Integer,
    'name':    fields.String
}


class FormatUser(object):
    def __init__(self, uid, name):
        self.user_id = uid
        self.name = name


# Define request parser
parser = reqparse.RequestParser()
parser.add_argument('name', help="Name cannot be blank")


def get_user(user_id):

    user = users.query.filter_by(id=user_id).first()
    try:
        if user:

            return FormatUser(user.id, user.name)

        else:

            return {'error': 'no such user found'}, 404

    except Exception as e:
        print(e)


# Resource-type class object to define functions for the RESTful API
class UserAPI(Resource):
    """
    Under resource objects, you can define functions corresponding to HTTP requests
    i.e. GET, POST, DELETE, etc.
    """

    # marshal_with will serialize the API response to follow schema
    @marshal_with(user_definition)
    def get(self, user_id):

        return get_user(user_id)

    @marshal_with(user_definition)
    def post(self, user_id):

        try:
            args = parser.parse_args()
            new_user = users(user_id, args['name'])
            db.session.add(new_user)
            db.session.commit()

            return FormatUser(user_id, args['name'])

        except Exception as e:
            print(e)

            return e

    def delete(self, user_id):

        try:
            user = users.query.filter_by(id=user_id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
            else:

                return {'error': 'no such user found'}, 404

        except Exception as e:

            return e


# Use the API object to connect the Resource objects to paths on the Flask server
# /<datatype: input_name> = a way to have variable paths
api.add_resource(UserAPI, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
