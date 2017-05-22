from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from app import db

class Types(db.Model):
    __tablename__ = 'Types'
    id = db.Column(db.Integer, primary_key = True)
    type_id = db.Column(db.Integer, unique = True)
    desc = db.Column(db.String(30))
    name = db.Column(db.String(30))

    def __init__(self, type_id = 0, desc = '', name = ''):
        self.type_id = type_id
        self.desc = desc
        self.name = name

    def __repr__(self):
        return '<Type %d: %r>' % (self.type_id, self.name)

