from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from cameras.models import Locations

# Create your views here.

@login_required(login_url='login')
def user_dashboard(request):
    
    list_locations = Locations.objects.all()
    return render(request , 'dashboard/dashboard.html',{'locations': list_locations})



def login_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')
    
def base_test(request):
    return render(request, 'base.html')