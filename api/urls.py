from django.urls import path
from .views import hello_world, cached_view

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('cached_view/', cached_view, name='hello_world'),
]
