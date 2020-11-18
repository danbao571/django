from django.urls import path
from . import views

urlpatterns = [
    path('', views.music, name='music'),
    path('get_song_url', views.get_song_url, name='get_song_url'),
    path('search_song', views.search_song, name='search_song'),
]
