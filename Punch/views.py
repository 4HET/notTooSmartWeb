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
        # ctx['username'] = request.POST['getUsername']
        # ctx['password'] = request.POST['getPassword']
        # print(ctx['rlt'])
    return render(request, "punch.html", ctx)

def mysql(sql, ty=0):
    conn = pymysql.connect(host="localhost",user="root", port=3306, passwd="123456", database="android")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    if ty==1:
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    else:
        cur.close()
        conn.close()
        return
if __name__ == '__main__':
    sql = 'show tables;'
    print(mysql(sql, 1))