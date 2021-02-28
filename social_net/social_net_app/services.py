from django.shortcuts import get_object_or_404
from social_net_app.models import User
import redis

redis_instance = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)
redis_instance.expire('current', 30)


def get_user(id_):
    return get_object_or_404(User, pk=id_)


def login_as(id_):
    redis_instance.sadd('current', id_)


def get_all_users():
    return User.objects.all()


def get_online_users():
    online_users_ids = [str(i) for i in redis_instance.smembers('current')]
    return User.objects.filter(id__in=online_users_ids)
