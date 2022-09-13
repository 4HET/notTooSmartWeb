import json

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
    print(type(class_info))


    # context = {
    #   "courseName": "大数据可视化分析",
    #   "startEndWeek": "2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17",
    #   "classPlace": "JS317",
    #   "teacherName": "陈矗",
    #   "classWeek": "2",
    #   "classSections": "0102"
    # }
    # print(context)

    return render(request, 'course.html', class_info)
