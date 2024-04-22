from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout


# Create your views here.

@login_required(login_url='login')
def user_dashboard(request):
    return render(request , 'dashboard/dashboard.html')


def user_logout(request):
    logout(request)
    return redirect('login')

def login_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')
    