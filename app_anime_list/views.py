from django.shortcuts import render
from django.views import generic
from .models import Anime, AnimeType

def index(request):
    num_anime_type = AnimeType.objects.count()
    num_anime = Anime.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_anime": num_anime,
        "num_anime_type": num_anime_type,
        "num_visits": num_visits + 1
    }

    return render(request, "app_anime_list/index.html",context=context)

class AnimeListView(generic.ListView):
    model = Anime
    template_name = "app_anime_list/anime_list.html"
    context_object_name = "anime_list"

    