from django.shortcuts import render

# Create your views here.
def mainActivity(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'mainActivity.html', context)