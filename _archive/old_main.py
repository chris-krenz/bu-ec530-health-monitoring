"""
https://github.com/TrevorChan1/EC530-flaskrestful-demo/tree/main/3.%20demo_with_database
https://stackoverflow.com/questions/73961938/flask-sqlalchemy-db-create-all-raises-runtimeerror-working-outside-of-applicat
"""

import os

from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '../database.db')
db = SQLAlchemy(app)


taskFields = {
    'id': fields.Integer,
    'name': fields.String,
}


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


class Items(Resource):
    @marshal_with(taskFields)
    def get(self):
        tasks = Task.query.all()
        return tasks

    @marshal_with(taskFields)
    def post(self):
        data = request.json
        task = Task(name=data['name'])
        db.session.add(task)
        db.session.commit()
        tasks = Task.query.all()
        return tasks


class Item(Resource):
    @marshal_with(taskFields)
    def get(self, pk):
        task = Task.query.filter_by(id=pk).first()
        return task

    @marshal_with(taskFields)
    def put(self, pk):
        data = request.json
        task = Task.query.filter_by(id=pk).first()
        task.name = data['name']
        db.session.commit()
        return task

    @marshal_with(taskFields)
    def delete(self, pk):
        task = Task.query.filter_by(id=pk).first()
        db.session.delete(task)
        db.session.commit()
        tasks = Task.query.all()
        return tasks


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return self.name


api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')


if __name__ == '__main__':
    app.run(debug=True)
