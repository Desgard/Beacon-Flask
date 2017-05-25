from flask import render_template, jsonify, request
from . import main
from app.main.params import public_params

from app import models
from app import db

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

@main.route('/beacon/v2/update_cache', methods = ['GET'])
def update_cache():
    return ''

@main.route('/beacon/v2/add_uuid', methods = ['GET'])
def add_user():
    return ''

@main.app_errorhandler(404)
def not_found(e):
    return jsonify({
        "msg": "api_not_found",
        "code": 404,
        "request": {
            "获取所有视频列表": "/beacon/v2/types",
            "获取每日5部影片": "/beacon/v2/top5",
        },
    })