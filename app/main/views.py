from flask import render_template, request, jsonify
from . import main

@main.route('/')
def index():
    return '<h1>Beacon API</h1>'

@main.route('/v2/top5')
def top_five():
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

@main.app_errorhandler(404)
def not_found(e):
    return jsonify({
        "msg": "api_not_found",
        "code": 404,
        "request": {
            "获取每日5部影片": "/v2/top5",
        },
    })