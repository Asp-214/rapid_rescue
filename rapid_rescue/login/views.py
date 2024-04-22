from django.shortcuts import redirect, render
from django.http import HttpResponse , JsonResponse

from django.contrib.auth import authenticate, login
from django.views.decorators.cache import never_cache
# from django.contrib.auth.decorators import login_required

# Create your views here.

@never_cache
def user_login(request):

    user = None
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        
        # else:
        #     return render(request, 'login.html',{'success': False, 'message': 'Incorrect username or password'})

    return render(request, 'login/login.html')