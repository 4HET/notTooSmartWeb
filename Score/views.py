import pprint

from django.shortcuts import render

from Score.score_info import get_cookie, get_score_info


# Create your views here.
def score(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')

    usr_info = {
        # "2020416094", "93999331Xj"
        "usr": username,
        "pwd": password
    }
    cookie = get_cookie(usr_info)
    print(cookie)

    score_info = get_score_info(cookie)
    score_info = eval(score_info.split(',"code":')[0] + "}")
    scoreList = []
    semesterOfYear = []
    for i in score_info['data']:
        scoreList.append({"scoreList": i['scoreList']})
        semesterOfYear.append({"semesterOfYear": i['semesterOfYear']})

    score_info = {"semesterOfYear": semesterOfYear, "scoreList": scoreList}

    pprint.pprint(score_info['semesterOfYear'])

    return render(request, 'score.html', score_info)