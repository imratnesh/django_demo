# api/views.py
from django.core.cache import cache
from django.http import JsonResponse

from .utils import get_hello_world


def hello_world(request):
    data = {'data': get_hello_world(), 'status': True}
    return JsonResponse(data)


def cached_view(request):
    """
    redis-cli
    keys *
    get new_key

    :param request:
    :return:
    """
    # Try fetching data from Redis cache
    data = cache.get('new_key')
    print(f"{data=}")
    if not data:
        # If not found, generate data and cache it
        data = {"message": "Hello from Redis Cache!"}
        cache.set('new_key', data, timeout=60 * 15)  # Cache for 15 minutes

    return JsonResponse(data)
