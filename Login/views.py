from django.shortcuts import render, redirect


# Create your views here.
def form(request):
    ctx = {}
    if request.POST:
        # ctx['rlt'] = request.POST['email']
        ctx['username'] = request.POST['username']
        ctx['password'] = request.POST['password']
        print(request.POST['username'])
        # print(ctx['rlt'])
    return render(request, 'login.html', ctx)

def login(request):
    ctx = {}
    if request.POST:
        # ctx['rlt'] = request.POST['email']
        ctx['username'] = request.POST['username']
        ctx['password'] = request.POST['password']
        print(request.POST['username'])
        # print(ctx['rlt'])
    return render(request, 'login.html', ctx)

def postForm(request):
    ctx = {}
    if request.POST:
        # ctx['rlt'] = request.POST['email']
        ctx['username'] = request.POST['username']
        ctx['password'] = request.POST['password']
        print(request.POST['username'])
        print(request.POST['password'])
    # return render(request, 'mainActivity.html', ctx)
    return redirect("/mainActivity/")
