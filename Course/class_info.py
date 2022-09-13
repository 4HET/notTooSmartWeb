import json

import requests


def get_class_info(cookie):
    headers = {
        'user-agent': 'Dart/2.13 (dart:io)',
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip',
        # 'cookie': cookie,
        'cookie': 'syt.sessionId=' + cookie['syt.sessionId'],
        # 'cookie': 'syt.sessionId=eb9b9576-aafb-4ab7-9a87-e10bfe659248',
        'host': '202.194.176.81:8080'
    }

    class_url = "http://202.194.176.81:8080/studentJwc/timetable"

    resp = requests.post(url=class_url, headers=headers).text

    # print(resp)
    return resp


def get_cookie(usr_info):
    usr = usr_info['usr']
    pwd = usr_info['pwd']

    user = {"username": usr, "password": pwd, "type": "student"}
    headers = {
        'user-agent': 'Dart/2.13 (dart:io)',
        'content-type':'application/json; charset=utf-8',
        'accept-encoding':'gzip'
    }
    login_url = "http://xuegong.qfnu.edu.cn:8080/authentication/login"

    session = requests.session()
    login = session.post(login_url, json=user, headers=headers)
    hd = login.headers
    # print(hd)
    cookies = session.cookies.get_dict()
    # print(cookies)

    return cookies

def dataFormat(data):
    data = json.loads(data)
    # print(data['data'])
    # print(len(data['data']))

if __name__ == '__main__':
    #usr为学号，pwd为密码，输入账号密码即可查询到课表
    usr_info = {
        # "2020416094", "93999331Xj"
        "usr": "2020416094",
        "pwd": "93999331Xj"
    }

    cookie = get_cookie(usr_info)
    print(cookie)
    class_info = get_class_info(cookie)
    # print(type(class_info))
    dataFormat(class_info)



