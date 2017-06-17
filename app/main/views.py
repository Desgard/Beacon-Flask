from flask import render_template, jsonify, request
from . import main
from app.main.params import public_params, get_user_id, is_have_user, write_video_to_db, get_write_video_to_db

from app import models, db
from datetime import datetime
from sqlalchemy import desc


import random
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

@main.route('/beacon/test/top5', methods = ['GET'])
def test_top_5():
    mv = models.Videos.query.all()
    res = []
    for index in range(0, 5):
        res.append(mv[index].toDict())
    print(res)
    return jsonify({
        'msg': 'test_for_top5',
        'code': 200,
        'datas': res,
    })

@main.route('/beacon/v2/top5', methods = ['GET', 'POST'])
def top_five():
    if request.method == 'GET':
        url = root_uri + 'batch/recommend'
        params = {
            'psp_uid': 1,
        }
        params.update(public_params)
        r = requests.get(url, params = params)
        if r.status_code == 200:
            res = []
            data = r.json()['data']
            for i in range(0, 5):
                video_list = data[i]['video_list']
                index = random.randint(0, 4)
                write_video_to_db(video_list[index])
                res.append(video_list[index])

            return jsonify({
                'msg': 'get_top_5_everyday',
                'code': 200,
                'datas': res,
            })
        else:
            return jsonify({
                'msg': 'network_error',
                'code': 210,
                'datas': [],
            })

    elif request.method == 'POST':
        url = root_uri + 'batch/channel'
        types = request.json['types']
        if len(types) > 0:
            res = []
            for type in types:
                params = {
                    'type': 'detail',
                    'channel_name': str(type),
                    'page_size': 4,
                    'version': 7.5,
                }
                params.update(public_params)
                r = requests.get(url, params = params)
                videos = r.json()['data']['video_list']
                # print(videos)
                aVideo = get_write_video_to_db(videos, len(videos) - 1)
                if aVideo is None:
                    return jsonify({
                        'msg': 'data_invalid',
                        'code': 206,
                    })
                res.append(aVideo.toDict())
                if len(res) == 5:
                    break

        if len(res) < 5:
            need_num = 5 - len(res)
            url = root_uri + 'batch/recommend'
            params = {
                'psp_uid': 1,
            }
            params.update(public_params)
            r = requests.get(url, params = params)
            if r.status_code is 200:
                data = r.json()['data']
                for i in range(0, need_num):
                    video_list = data[i]['video_list']
                    index = random.randint(0, 4)
                    write_video_to_db(video_list[index])
                    res.append(video_list[index])


        return jsonify({
            "msg": "today_top_5_filems",
            "code": 200,
            "datas": res,
        })

@main.route('/beacon/v2/guess_you_like', methods = ['GET'])
def guess_you_like():
    videos = models.Videos.query.all()
    cnt = 0
    res = []
    for video in videos:
        res.append(video.toDict())
        cnt += 1
        if cnt is 20:
            break
    return jsonify({
        "msg": "guess_you_like",
        "count": cnt,
        "code": 200,
        "datas": res,
    })

@main.route('/beacon/v2/add_like_video', methods = ['POST'])
def add_like_video():
    uuid = request.json['uuid']
    video_id = request.json['video_id']

    if is_have_user(uuid) is False:
        add_user(uuid)
    userItem = models.Users.query.filter_by(uuid = uuid).first()
    vidoeItem = models.Videos.query.filter_by(video_id = video_id).first()

    if vidoeItem is None or userItem is None:
        return jsonify({
            'msg': 'data_invalid',
            'code': 205,
        })

    for lov in userItem.like_videos:
        if vidoeItem == lov:
            return jsonify({
                'msg': 'it_is_like_video',
                'code': 206,
            })

    userItem.like_videos.append(vidoeItem)


    db.session.add(userItem)
    db.session.commit()
    return jsonify({
        'msg': 'add_like_success',
        'code': 200,
    })

@main.route('/beacon/v2/get_like_video/<uuid>', methods = ['GET'])
def get_like_video(uuid):
    if is_have_user(uuid) is False:
        return jsonify({
            'msg': 'user_not_exists',
            'code': 206,
        })
    user = models.Users.query.filter_by(uuid = uuid).first()
    videos = user.like_videos
    res = []
    for video in videos:
        res.append(video.toDict())
    return jsonify({
        'msg': 'get_all_like_videos',
        'code': 200,
        'data': res,
    })

@main.route('/beacon/v2/del_like_video', methods = ['POST'])
def del_like_video():
    uuid = request.json['uuid']
    video = request.json['video_id']
    users = models.Users.query.filter_by(uuid = uuid)
    if users.count() is 0:
        return jsonify({
            'msg': 'user_not_exists',
            'code': 206,
        })
    user = users.first()
    like_videos = user.like_videos
    for like_video in like_videos:
        if str(like_video.a_id) == str(video):
            sel = like_video
            user.like_videos.remove(sel)
            db.session.commit()
            return jsonify({
                'msg': 'del_success',
                'code': 200
            })
    return jsonify({
        'msg': 'video_not_exists',
        'code': 206,
    })

@main.route('/beacon/v2/add_play_history', methods = ['POST'])
def add_play_history():
    uuid = request.json['uuid']
    video = request.json['video_id']

    if is_have_user(uuid) is False:
        add_user(uuid)

    item = models.Histories.query.filter_by(video_id = video, user_id = uuid).first()
    if item == None:
        history_item = models.Histories(video_id = video, user_id = uuid)
        db.session.add(history_item)
        db.session.commit()
        return jsonify({
            'msg': 'add_history_item',
            'code': 200
        })
    else:
        item.watch_date = datetime.now()
        db.session.add(item)
        db.session.commit()
        return jsonify({
            'msg': 'record_success',
            'code': 200,
        })


@main.route('/beacon/v2/get_play_history/<uuid>', methods = ['GET'])
def get_play_history(uuid):
    if is_have_user(uuid) is False:
        return jsonify({
            'msg': 'user_not_exists',
            'code': 206
        })
    histories = models.Histories.query.order_by(desc(models.Histories.watch_date)).all()
    res = []
    for history in histories:
        video_id = history.video_id
        search_res = models.Videos.query.filter_by(video_id = video_id)
        item = dict()
        if search_res.count() > 0 :
            video = search_res[0]
            item = video.toDict()
        item["watch_date"] = history.watch_date
        res.append(item)
    return jsonify({
        'msg': 'get_all_histories',
        'code': 200,
        'data': res,
    })

@main.route('/beacon/v2/del_play_history', methods = ['POST'])
def del_play_history():
    uuid = request.json['uuid']
    video = request.json['video_id']

    sels = models.Histories.query.filter_by(user_id = uuid, video_id = video)
    if sels.count() is 0:
        return jsonify({
            'msg': 'item_not_exists',
            'code': 206,
        })
    sel = sels.first()
    print(sel)
    db.session.delete(sel)
    db.session.commit()
    return jsonify({
        'msg': 'del_success',
        'code': 200,
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



