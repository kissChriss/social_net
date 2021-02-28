from .services import get_all_users, get_user, get_online_users, login_as
from django.shortcuts import render


def index(request):
    return render(request, "index.html", {'users': get_all_users()})


def user(request, id_):
    if request.method == 'GET':
        login_as(id_)
        return render(request, "user.html", {'user': get_user(id_), 'users': get_online_users()})
