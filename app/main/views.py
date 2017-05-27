from flask import render_template, jsonify, request
from . import main
from app.main.params import public_params, get_user_id, is_have_user

from app import models, db
from datetime import datetime

import requests

root_uri = 'http://iface.qiyi.com/openapi/'

@main.route('/beacon')
def index():
    return '<h1>Beacon API</h1>'

@main.route('/beacon/v2/types')
def get_types():
    url = root_uri + 'batch/channel'
    params = {
        'type': 'list',
        'version': 7.5,
    }
    params.update(public_params)
    r = requests.get(url, params = params)
    if r.status_code == 200:
        return jsonify({
            'msg': 'all_types',
            'code': '200',
            'datas': r.json()['data'],
        })
    else:
        return jsonify({
            'msg': 'error',
            'code': r.status_code,
            'datas': [],
        })


@main.route('/beacon/v2/top5', methods = ['GET', 'POST'])
def top_five():
    if request.method == 'GET':
        print('GET')

    return jsonify({
        "msg": "today_top_5_filems",
        "code": 200,
        "datas": [
            "file1",
            "file2",
            "file3",
            "file4",
            "file5",
        ],
    })

@main.route('/beacon/v2/add_like_video', methods = ['POST'])
def add_like_video():
    uuid = request.json['uuid']
    video_id = request.json['video_id']

    if is_have_user(uuid) is False:
        return jsonify({
            'msg': 'user_already_exists',
            'code': '206',
        })
    userItem = models.Users.query.filter_by(uuid = uuid).first()
    vidoeItem = models.Videos.query.filter_by(movie_id = video_id).first()

    if vidoeItem is None or userItem is None:
        return jsonify({
            'msg': 'data_invalid',
            'code': '205',
        })

    userItem.like_videos.append(vidoeItem)
    db.session.add(userItem)
    db.session.commit()
    return jsonify({
        'msg': 'add_success',
        'code': '200',
    })


@main.route('/beacon/v2/add_play_history', methods = ['POST'])
def add_play_history():
    uuid = request.json['uuid']
    video = request.json['video_id']

    # TODO: 对格式进行检测
    if is_have_user(uuid) is False:
        return jsonify({
            'msg': 'user_already_exists',
            'code': '206',
        })

    user_id = get_user_id(uuid)
    item = models.Histories.query.filter_by(video_id = video, user_id = user_id).first()
    if item == None:
        history_item = models.Histories(video_id = video, user_id = uuid)
        db.session.add(history_item)
        db.session.commit()
        return jsonify({
            'msg': 'add_history_item',
            'code': '200'
        })
    else:
        item.watch_date = datetime.now()
        db.session.add(item)
        db.session.commit()
        return jsonify({
            'msg': 'record_success',
            'code': '200',
        })

@main.route('/beacon/v2/add_uuid/<uuid>', methods = ['GET'])
def add_user(uuid):
    user = models.Users(uuid = uuid)
    db.session.add(user)
    db.session.commit()

    if is_have_user(uuid):
        return jsonify({
            'msg': 'new_user_write',
            'code': 200,
        })
    else:
        return jsonify({
            'msg': 'user_already_exists',
            'code': 206,
        })


@main.app_errorhandler(404)
def not_found(e):
    return jsonify({
        "msg": "api_not_found",
        "code": 404,
        "request": {
        },
    })



