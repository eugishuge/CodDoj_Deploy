from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User


# Create your views here.
def index (request):
    return render(request, 'login_templates/index.html')

def login(request):
    _login = User.objects.login(request.POST)

    if _login == True:
        request.session['email'] = request.POST['email']
        return redirect ('/quotes')
    else:
        for x in _login[1]:
            messages.error(request, x)
        return redirect('/')

def register(request):
    _register = User.objects.register(request.POST)

    if _register == True:
        request.session['email'] = request.POST['email']
        return redirect ('/quotes')
    else:
        for x in _register[1]:
            messages.error(request, x)
        print 'registration failed'
        return redirect ('/')

def quotes (request):
    return redirect ('/bb2/quotes')
