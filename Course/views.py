import json
import pprint

from django.shortcuts import render

from Course.class_info import get_cookie

from Course.class_info import get_class_info


# Create your views here.
def course(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')

    usr_info = {
        # "2020416094", "93999331Xj"
        "usr": username,
        "pwd": password
    }
    cookie = get_cookie(usr_info)

    class_info = get_class_info(cookie)
    # class_info = dict(class_info)
    class_info = eval(class_info.split(',"code":')[0]+"}")
    # print(class_info)
    # print(type(class_info))

    dic = {}
    for i in range(1, 12):
        s = str(i)
        dic[s] = {'date': s}
    # print(dic)

    data = class_info['data']
    for i in data:
        info = i['courseName'] + '@' + i['classPlace']
        week = i['classWeek']

        for j in range(0, len(i['classSections']), 2):
            no = i['classSections'][j:j+2]
            no = str(int(no))
            dic[no][week] = info


    # print(dic)

    end = []
    for i in range(1, len(dic) + 1):
        end.append(dic[str(i)])
    pprint.pprint(end)
    # context = {
    #   "courseName": "大数据可视化分析",
    #   "startEndWeek": "2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17",
    #   "classPlace": "JS317",
    #   "teacherName": "陈矗",
    #   "classWeek": "2",
    #   "classSections": "0102"
    # }
    # print(context)

    return render(request, 'course.html', {'end': end})
