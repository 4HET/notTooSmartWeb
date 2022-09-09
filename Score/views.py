from django.shortcuts import render

# Create your views here.
def score(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'score.html', context)