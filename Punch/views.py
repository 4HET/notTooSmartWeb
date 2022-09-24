'''
AndroidServer Punch URL Configuration
views
'''
import pymysql
from django.shortcuts import render, redirect

from Punch import models

from Punch.models import User


# Create your views here.
def punch(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/login/')

    user_obj = models.User.objects.filter(username=username, password=password).first().isPunch
    if user_obj:
        return redirect('/isPunch/')
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['email']
        # ctx['username'] = request.POST['username']
        # ctx['password'] = request.POST['password']
        print(request.POST['email'])
        user1 = User.objects.get(username=username)
        user1.isPunch = True
        user1.email = request.POST['email']
        user1.save()
        return redirect('/isPunch/')
        # print(ctx['rlt'])
    return render(request, "punch.html", ctx)

def isPunch(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    user1 = User.objects.get(username=username)
    email = user1.email
    context = {}
    context['email'] = email
    context['username'] = username
    context['password'] = password
    print(email)
    print(username)
    print(password)
    return render(request, "isPunch.html", context)

def postRequest(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/login/')

    user_obj = models.User.objects.filter(username=username, password=password).first().isPunch
    if user_obj:
        return redirect('/isPunch/')
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['email']
        # ctx['username'] = request.POST['username']
        # ctx['password'] = request.POST['password']
        print(request.POST['email'])
        user1 = User.objects.get(username=username)
        user1.isPunch = True
        user1.email = request.POST['email']
        user1.save()
        return redirect('/isPunch/')
        # print(ctx['rlt'])
    return render(request, "punch.html", ctx)


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(username, password)

    try:
        user_obj = models.User.objects.filter(username=username, password=password).first()
        print(user_obj.username)
        print(user_obj.password)
    except:
        user_obj = False

    if not user_obj:
        return redirect("/login/")
    else:
        rep = redirect("/mainActivity/")
        rep.set_cookie("is_login", True)
        rep.set_cookie("username", username)
        rep.set_cookie("password", password)
        return rep

def index(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/login/')
    return render(request, "index.html")

def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    return rep  # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面


def order(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, "order.html")

def deletePunch(request):
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    # print(username)
    # user_obj = models.User.objects.filter(username=username, password=password).first()
    user1 = User.objects.get(username=username)
    user1.isPunch = False
    user1.email = ""

    user1.save()
    return redirect('/punch/')

if __name__ == '__main__':
    sql = 'show tables;'
    # print(mysql(sql, 1))