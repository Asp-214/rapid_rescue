from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def respond(request):
    return render(request , 'users/users.html')
