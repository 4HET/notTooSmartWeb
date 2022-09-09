from django.shortcuts import render

# Create your views here.
def course(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'course.html', context)