from django.test import TestCase
from django.contrib.auth.models import User
from app_anime_list.models import AnimeType, Anime


class AnimeTypeModelTest(TestCase):
    def setUp(self):
        self.anime_type = AnimeType.objects.create(name="Shounen")

    def test_anime_type_name(self):
        self.assertEqual(str(self.anime_type), "Shounen")


class AnimeModelTest(TestCase):
    def setUp(self):
        self.anime_type = AnimeType.objects.create(name="Shounen")
        self.anime = Anime.objects.create(
            name="My Anime",
            description="Anime description",
            type=self.anime_type,
            episodes=12,
            my_episode=5,
            my_rating=8,
        )

    def test_anime_str_representation(self):
        expected_str = "My Anime Rating: 8 Shounen | 5/12"
        self.assertEqual(str(self.anime), expected_str)


class AnimeAdminTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="admin"
        )
        self.client.login(username="admin", password="admin")
        self.anime_type = AnimeType.objects.create(name="Shounen")
        self.anime = Anime.objects.create(
            name="My Anime",
            description="Anime description",
            type=self.anime_type,
            episodes=12,
            my_episode=5,
            my_rating=8,
        )

    def test_anime_admin_list_view(self):
        response = self.client.get("/admin/app_anime_list/anime/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Anime")

    def test_anime_admin_detail_view(self):
        response = self.client.get(f"/admin/app_anime_list/anime/{self.anime.id}/change/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Anime")
