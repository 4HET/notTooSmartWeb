import json

import requests


def get_score_info(cookie):
    headers = {
        'user-agent': 'Dart/2.13 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        # 'cookie': cookie,
        'cookie': 'syt.sessionId=' + cookie['syt.sessionId'],
        # 'cookie': 'syt.sessionId=eb9b9576-aafb-4ab7-9a87-e10bfe659248',
        'host': '202.194.176.81:8080'
    }

    score_url = "http://202.194.176.81:8080/studentJwc/score"

    resp = requests.post(url=score_url, headers=headers).text

    # print(resp)
    return resp


def get_cookie(usr_info):
    usr = usr_info['usr']
    pwd = usr_info['pwd']

    user = {"username": usr, "password": pwd, "type": "student"}
    headers = {
        'user-agent': 'Dart/2.13 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip'
    }
    login_url = "http://xuegong.qfnu.edu.cn:8080/authentication/login"

    session = requests.session()
    login = session.post(login_url, json=user, headers=headers)
    cookies = session.cookies.get_dict()
    # print(cookies)

    return cookies


if __name__ == '__main__':
    usr_info = {
        "usr": "2020416089",
        "pwd": "LZYsb666"
    }
    cookie = get_cookie(usr_info)
    print(cookie)

    score_info = get_score_info(cookie)
    print(score_info)
