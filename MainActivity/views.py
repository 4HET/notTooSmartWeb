from django.shortcuts import render

# Create your views here.
def mainActivity(request):
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