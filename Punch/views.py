'''
AndroidServer Punch URL Configuration
views
'''
import pymysql
from django.shortcuts import render


# Create your views here.
def punch(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'punch.html', context)

def postRequest(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['email']
        ctx['username'] = request.POST['username']
        ctx['password'] = request.POST['password']
        # print(ctx['rlt'])
    return render(request, "punch.html", ctx)

if __name__ == '__main__':
    sql = 'show tables;'
    # print(mysql(sql, 1))