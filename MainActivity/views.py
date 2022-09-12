from django.shortcuts import render, redirect

from Punch import models


# Create your views here.
def mainActivity(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/login/')

    # username = request.COOKIES.get('username')
    # password = request.COOKIES.get('password')
    #
    # user_obj = models.User.objects.filter(username=username, password=password).first().isPunch
    # if not user_obj:
    #     return redirect('/index/')

    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'mainActivity.html', context)

def usrInfo(request):
    ctx = {}
    if request.POST:
        ctx['username'] = request.POST['username']
        ctx['password'] = request.POST['password']
        print(request.POST['username'])
        print(request.POST['password'])
        # print(ctx['rlt'])
    return render(request, "mainActivity.html", ctx)