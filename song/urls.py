from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


app_name = 'song'
urlpatterns = [
    path('', views.MusicView.as_view(), name='music'),
    path('get_song_url', views.get_song_url, name='get_song_url'),
    path('search_song', views.search_song, name='search_song'),
    path('remove_bg', csrf_exempt(views.remove_bg), name='remove_bg'),
    path('download_music', views.download_music, name='download_music'),
]
