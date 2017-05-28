from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

UserVideoRelation = db.Table('UserVideoRelation',
    db.Column('videos_id', db.Integer, db.ForeignKey('Videos.id')),
    db.Column('users_id', db.Integer, db.ForeignKey('Users.id'))
)

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    uuid = db.Column(db.String(20), index = True)

    def __init__(self, uuid = ''):
        self.uuid = uuid

    like_videos = db.relationship('Videos',
                                  secondary = UserVideoRelation,
                                  backref = db.backref('Users', lazy = 'dynamic'))
    def __repr__(self):
        return '<User id: %d, uuid: %r>' % (self.id, self.uuid)

class Histories(db.Model):
    __tablename__ = 'Histories'
    id = db.Column(db.Integer, primary_key = True)
    video_id = db.Column(db.Integer)
    watch_date = db.Column(db.DateTime, default = datetime.now)
    user_id = db.Column(db.Integer, index = True)

    def __init__(self, video_id = -1, user_id = -1):
        self.video_id = video_id
        self.watch_date = datetime.now()
        self.user_id = user_id

    def toDict(self):
        res = dict()
        res['video_id'] = self.video_id
        res['watch_date'] = self.watch_date
        res['user_id'] = self.user_id
        return res

class Types(db.Model):
    __tablename__ = 'Types'
    id = db.Column(db.Integer, primary_key = True)
    type_id = db.Column(db.Integer, index = True)
    desc = db.Column(db.String(30))
    name = db.Column(db.String(30))

    def __init__(self, type_id = 0, desc = '', name = ''):
        self.type_id = type_id
        self.desc = desc
        self.name = name

    def __repr__(self):
        return '<Type %d: %r>' % (self.type_id, self.name)

    def toDict(self):
        res = dict()
        res['id'] = self.type_id
        res['desc'] = self.desc
        res['name'] = self.name
        return res

class Videos(db.Model):
    __tablename__ = 'Videos'
    id = db.Column(db.Integer, primary_key = True)
    video_id = db.Column(db.String(20), unique = True, index = True)
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
        self.img = str(img)
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
        return '<Video %r: %r>' % (self.video_id, self.title)

    def toDict(self):
        res = dict()
        res['id'] = self.video_id
        res['title'] = self.title
        res['short_title'] = self.short_title
        res['img'] = self.img
        res['sns_score'] = self.sns_score
        res['play_count'] = self.play_count
        res['play_count_text'] = self.play_count_text
        res['a_id'] = self.a_id
        res['tv_id'] = self.tv_id
        res['is_vip'] = self.is_vip
        res['type'] = self.type
        res['p_type'] = self.p_type
        res['date_timestamp'] = self.date_timestamp
        res['date_format'] = self.date_format
        res['total_num'] = self.total_num
        res['update_num'] = self.update_num
        return res
