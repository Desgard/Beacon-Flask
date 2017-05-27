from app import models

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

def get_user_id(uuid):
    if is_have_user(uuid):
        user = models.Users.query.filter_by(uuid = str(uuid)).first()
        return user.id