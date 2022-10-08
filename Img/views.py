import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from Img.models import IMG


# Create your views here.
def img(request):
    username = request.COOKIES.get('username')
    img = IMG.objects.filter(username=username)
    if img.count() != 0:
        return redirect('/showImg/')
    if request.method == 'POST':
        if img.count() != 0:
            img = IMG.objects.get(username=username)
            img.img = request.FILES.get('img')
            img.name = request.FILES.get('img').name
            print(img.img.url)
            img.save()
        else:
            new_img = IMG(
                img=request.FILES.get('img'),
                name=request.FILES.get('img').name,
                # name=username+'.'+request.FILES.get('img').name.split('.')[1],
                username=request.COOKIES.get('username')
            )
            new_img.save()

        # return HttpResponse("<p>数据添加成功！</p>")
        return render(request, 'showImg.html')
    return render(request, 'img.html')


def showImg(request):

    username = request.COOKIES.get('username')
    imgs = IMG.objects.filter(username=username)
    content = {
        'imgs': imgs,
    }
    return render(request, 'showimg.html', content)
