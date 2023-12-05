from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# view : takes in a req and provides res
# req handler 

def say_Hello(request): 
    # return HttpResponse('Hello World')
    x = 1
    y = 2
    return render(request, 'hello.html', {
        'name' : 'Nikhil'
    })