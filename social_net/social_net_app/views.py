from django.http import HttpResponse
from social_net_app.models import User
from django.shortcuts import render


def index(request):
    users = User.objects.all()
    return render(request, "index.html", context = {'users': users})
