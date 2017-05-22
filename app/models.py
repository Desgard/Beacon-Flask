from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from app import db

class Types(db.Model):
    __tablename__ = 'Types'
    id = db.Column(db.Integer, primary_key = True)
    type_id = db.Column(db.Integer, unique = True, index = True)
    desc = db.Column(db.String(30))
    name = db.Column(db.String(30))

    def __init__(self, type_id = 0, desc = '', name = ''):
        self.type_id = type_id
        self.desc = desc
        self.name = name

    def __repr__(self):
        return '<Type %d: %r>' % (self.type_id, self.name)

class Videos(db.Model):
    __tablename__ = 'Videos'
    id = db.Column(db.Integer, primary_key = True)
    video_id = db.Colmn(db.String(20), unique = True, index = True)
    title = db.Column(db.String(50))
    short_title = db.Column(db.String(50))
    img = db.Column(db.String(1000))
    sns_score = db.Column(db.String(100))
    play_count = db.Column(db.String(100))
    play_count_text = db.Column(db.String(20))
    a_id = db.Column(db.String(20))
    tv_id = db.Column(db.String(20))
    is_vip = db.Column(db.String(10))
    type = db.Column(db.String(20))
    p_type = db.Column(db.String(10))
    date_timestamp = db.Column(db.String(20))
    date_format = db.Column(db.String(20))
    total_num = db.Column(db.String(10))
    update_num = db.Column(db.String(10))

    def __init__(self, video_id = '', title = '', short_title = '', img = '', sns_score = '', play_count = '', play_count_text = '', a_id = '', tv_id = '', is_vip = '', type = '', p_type = '',
                 date_timestamp = '', date_format = '', total_num = '', update_num = ''):
        self.video_id = video_id
        self.title = title
        self.short_title = short_title
        self.img = img
        self.sns_score = sns_score
        self.play_count = play_count
        self.play_count_text = play_count_text
        self.a_id = a_id
        self.tv_id = tv_id
        self.is_vip = is_vip
        self.type = type
        self.p_type = p_type
        self.date_timestamp = date_timestamp
        self.date_format = date_format
        self.total_num = total_num
        self.update_num = update_num

    def __repr__(self):
        return '<Video %d: %r>' % (self.video_id, self.title)
