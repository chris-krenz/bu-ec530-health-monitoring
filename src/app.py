"""
Basic functionality based on: https://github.com/TrevorChan1/EC530-flaskrestful-demo/tree/main/3.%20demo_with_database

Other references:
https://medium.com/@dennisivy/my-first-crud-app-with-fast-api-74ac190d2dcc
https://medium.com/@dennisivy/flask-restful-crud-api-c13c7d82c6e5
https://stackoverflow.com/questions/73961938/flask-sqlalchemy-db-create-all-raises-runtimeerror-working-outside-of-applicat
"""
import os

from flask import Flask, jsonify, request, session, make_response
# from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
# from flask_restful import Resource, Api, fields, marshal_with, reqparse
from flask_restx import Resource, Api, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from requests import post, get, delete

# from CONFIG import ROOT_DIR
# import CONFIG
# from src.utils.misc.sanitizer import sanitizer


# Connect to local '../data/database.db' SQLite file
app = Flask(__name__)
# app.secret_key = b'***************************************'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data',
                                                                    'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
api = Api(app)
# bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

''' Standard SQL Commands
(https://www.freecodecamp.org/news/basic-sql-commands/)
CREATE TABLE users (id INT PRIMARY KEY, name TEXT NOT NULL);  -- Create new table
SELECT name FROM users WHERE id = 1;  -- Retrieve filtered data; DELETE to del record instead
ALTER TABLE main.users DROP COLUMN secret;  -- Delete a column from a table; ADD to add col instead
'''

'''cURL Command Examples
curl -H "Content-Type: application/json" -d '{"name":"foo"}' http://localhost:8000/api/user/3
# (failed) curl http://localhost:8000/api/user -d "name=foo" -X PUT
'''


def sanitizer(message: bytes | str) -> str:
    """
    Sanitize message to ensure not malicious.  Primarily filters out SQL Queries.
    Raises exception if match is found; otherwise returns string indicating message is clean.
    The coincidental combination of these words with a ';' is relatively unlikely.
    Will be false positives, but erring on the side of safety.
    """
    message = message.decode() if type(message) == bytes else message
    message = str(message)
    # (must also contain a ';')
    restricted_sql = [['select',   'from'],
                      ['drop',     'database'],
                      ['drop',     'table'],
                      ['drop',     'index'],
                      ['update',   'set'],
                      ['delete',   'from'],
                      ['alter',    'table'],
                      ['grant',    'to'],
                      ['revoke',   'from'],
                      ['truncate', 'table'],
                      ['rollback', 'to']]

    if ';' in message:
        for keyword_set in restricted_sql:
            if any([(keyword in message.lower()) for keyword in keyword_set]):
                raise RuntimeError('You entered illegal characters, please try again...')

    return 'Submitted message clean...'


# Define SQLite table schema
class users(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(20), nullable=False)
    ssn   = db.Column(db.String(255))
    email = db.Column(db.String(255))
    role  = db.Column(db.String(255))

    def __init__(self, id, name, ssn, email, role):
        self.id    = id
        self.name  = name
        self.ssn   = ssn
        self.email = email
        self.role  = role

    def __repr__(self):
        return self.name


# Define output data schema
user_definition = api.model('User', {
    'user_id': fields.Integer,
    'name':    fields.String,
    'ssn':     fields.String,
    'email':   fields.String,
    'role':    fields.String
})


class FormatUser(object):
    def __init__(self, uid, name, ssn, email, role):
        self.user_id = uid
        self.name = name
        self.ssn = ssn
        self.email = email
        self.role = role


class FormatString(object):
    def __init__(self, data):
        self.data = data


# Define request parser
# NOTE: This pattern has been deprecated; flask-restx will transition to marshmallow-like approach
parser = reqparse.RequestParser()
parser.add_argument('name',  help="Name cannot be blank")
parser.add_argument('ssn',   help="SSN cannot be blank")
parser.add_argument('email', help="email cannot be blank")
parser.add_argument('role',  help="Role cannot be blank")


def get_user(user_id):

    user = users.query.filter_by(id=user_id).first()
    try:
        if user:

            return FormatUser(user.id, user.name, user.ssn, user.email, user.role)

        else:

            return {'error': 'no such user found'}, 404

    except Exception as e:
        print(e)


@api.doc()
@api.route('/api/users/<int:user_id>')
class UserAPI(Resource):

    # marshal_with will serialize the API response to follow schema
    @marshal_with(user_definition)
    def get(self, user_id):
        print(sanitizer(str(user_id)))
        print('GET-ing', user_id, '...')

        return get_user(user_id)

    @marshal_with(user_definition)
    def put(self, user_id):
        print(sanitizer(user_id))
        print('PUT-ing', user_id, '...')
        try:
            args = parser.parse_args()
            for arg in args.values():
                print(sanitizer(str(arg)))
            new_user = users(user_id, args['name'], args['ssn'], args['email'], args['role'])
            db.session.add(new_user)
            db.session.commit()

            return FormatUser(user_id, args['name'], args['ssn'], args['email'], args['role'])

        except Exception as e:
            print('ERROR: ', e)
            return FormatString(e)

    @marshal_with(user_definition)
    def delete(self, user_id):
        print(sanitizer(str(user_id)))
        print('DELETE-ing', user_id, '...')
        try:
            user = users.query.filter_by(id=user_id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
            else:

                return {'error': 'no such user found'}, 404

        except Exception as e:
            print(e)
            return e


# Native Flask alternative
@app.route('/api')
def backend_health_check():
    return 'Server is functioning'

# Flask-Restful alternative
# api.add_resource(UserAPI, '/api/users/<int:user_id>')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
