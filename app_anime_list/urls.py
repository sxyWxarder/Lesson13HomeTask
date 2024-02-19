from django.urls import path
from .views import (
    index, 
    AnimeListView 
)

urlpatterns = [
    path("", index, name="index"),
    path("anime/", AnimeListView.as_view(), name="anime-list" )
]

app_name = "app_anime_list"

