from django.shortcuts import render, redirect, reverse
from ..login.models import User
from .models import Quotes, Join
from django.contrib import messages
from sets import Set

# Create your views here.
def quotes (request):
    all_users = User.objects.all()
    all_quotes = Quotes.objects.all()
    all_join = Join.objects.all()
    all_join_fave = Join.objects.filter(all_users__email = request.session['email'])

    a = set(Quotes.objects.all())
    b = set(Quotes.objects.filter(everything__all_users__email=request.session['email']))

    remove = (a.difference(b))

    context = {
    "all_users": all_users,
    "all_quotes" : all_quotes,
    "all_join" : all_join,
    "all_join_fave": all_join_fave,
    'remove': remove
    }
    return render(request, 'bb2_templates/quotes.html', context)

def contribute(request):
    session = request.session['email']

    _contribute = Quotes.objects.quote(request.POST, session)

    user_quote = User.objects.filter(email = request.session['email'])

    if _contribute == True:
        Join.objects.create(all_users = user_quote[0], all_quotes = Quotes.objects.latest('id'))
        return redirect ('/bb2/quotes')
    else:
        for x in _contribute[1]:
            messages.error(request, x)
        return redirect ('/bb2/quotes')

def user_info(request, _id):
        all_users = Join.objects.filter(all_users__id = _id)
        all_join = Join.objects.all()

        count = Join.objects.filter(all_users__id = _id).count

        context = {
        "all_users": all_users,
        "all_join" : all_join,
        "count": count
        }
        return render(request, 'bb2_templates/user_info.html', context)

def favorites (request, _qid):
    add_quote = Quotes.objects.filter(id = _qid)
    add_fave = User.objects.filter(email = request.session['email'])

    Join.objects.create(all_quotes = add_quote[0], all_users = add_fave[0])
    return redirect ('/bb2/quotes')

def remove (request, _qid):
    Join.objects.filter(all_users__email=request.session['email']).filter(all_quotes__id=_qid).delete()
    return redirect('/bb2/quotes')

def logout(request):
    request.session.clear()
    return redirect ('/')
