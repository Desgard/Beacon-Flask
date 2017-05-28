from app import models, db

public_params = {
    'app_k': 'f0f6c3ee5709615310c0f053dc9c65f2',
    'app_v': 8.4,
    'app_t': 0,
    'platform_id': 10,
    'dev_os': 6.0,
    'dev_ua': 'iPhone9,3',
    'dev_hw': '{"cpu":0, "gpu":"", "mem":"50.4MB"}',
    'net_sts': 1,
    'scrn_sts': 1,
    'scrn_res': 1334*750,
    'scrn_dpi': 153600,
    'qyid': '87390BD2-DACE-497B-9CD4-2FD14354B2A4',
    'secure_p': 1,
    'secure_v': 'iPhone',
    'core': 1,
    'req_sn': 1493946331320,
    'req_times': 1,
}

def is_have_user(uuid):
    search_res = models.Users.query.filter_by(uuid=str(uuid)).count()
    if search_res == 0:
        return False
    else:
        return True

def is_have_video(id):
    search_res = models.Videos.query.filter_by(video_id=str(id)).count()
    if search_res == 0:
        return False
    else:
        return True

def get_user_id(uuid):
    if is_have_user(uuid):
        user = models.Users.query.filter_by(uuid = str(uuid)).first()
        return user.id

def write_video_to_db(video):
    video_id = video['id']
    if is_have_video(video_id):
        return False

    db_video = models.Videos(video_id = video['id'],
                             title=video['title'],
                             short_title=video['short_title'],
                             img=video['img'],
                             sns_score=video['sns_score'],
                             play_count=video['play_count'],
                             play_count_text=video['play_count_text'],
                             a_id=video['a_id'],
                             tv_id=video['tv_id'],
                             is_vip=video['is_vip'],
                             type=video['type'],
                             p_type=video['p_type'],
                             date_timestamp=video['date_timestamp'],
                             date_format=video['date_format'],
                             total_num=video['total_num'],
                             update_num=video['update_num'])

    db.session.add(db_video)
    db.session.commit()
    return True

def get_write_video_to_db(videosDic, index):
    if index > len(videosDic):
        return None
    video = videosDic[index]
    db_video = models.Videos(video_id = video['id'],
                             title=video['title'],
                             short_title=video['short_title'],
                             img=video['img'],
                             sns_score=video['sns_score'],
                             play_count=video['play_count'],
                             play_count_text=video['play_count_text'],
                             a_id=video['a_id'],
                             tv_id=video['tv_id'],
                             is_vip=video['is_vip'],
                             type=video['type'],
                             p_type=video['p_type'],
                             date_timestamp=video['date_timestamp'],
                             date_format=video['date_format'],
                             total_num=video['total_num'],
                             update_num=video['update_num'])
    isHave = models.Videos.query.filter_by(video_id = db_video.video_id).count()
    if isHave is 0:
        db.session.add(db_video)
        db.session.commit()
    return db_video


