from django.shortcuts import render
from django.contrib.auth.decorators import login_required 



# Create your views here.

@login_required(login_url='login')
def show_users(request):
    return render(request,'users/users.html')


@login_required(login_url='login')
def create_user(request):  
    return render(request,'users/create_user.html')


@login_required(login_url='login')
def modify_user(request):
    return render(request,'users/create_user.html')