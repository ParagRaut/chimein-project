from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home-page')
        else:
            errorcontext = {'error': 'Error, the username or passwords is incorrect :( '}
            return render(request, 'accounts/login_page.html', errorcontext)
    else:
        context = {}
        return render(request, 'accounts/login_page.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home-page')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                errorcontext = {'error': 'Error, The Username is already taken :( '}
                return render(request, 'accounts/signup_page.html', errorcontext)
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                auth.login(request, user)
                return redirect('home-page')
        else:
            errorcontext = {'error': 'Error, the Passwords should match :( '}
            return render(request, 'accounts/signup_page.html', errorcontext)

    else:
        context = {}
        return render(request, 'accounts/signup_page.html', context)
