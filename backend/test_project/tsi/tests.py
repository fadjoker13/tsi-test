from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Player
from .average import average_stats

class PlayerApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.player_data = {'name': 'Lebron James', 'jersey_num': 23, 'position': 'Forward'}
        self.player = Player.objects.create(**self.player_data)
        self.url = reverse('players-list')
    def test_get_players_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class DataProcessingTests(TestCase):
    def test_calculate_average_performance(self):
        game_statistics = [
            {'points': 20, 'assists': 5},
            {'points': 15, 'assists': 3},
        ]
        average = average_stats(game_statistics)
        self.assertEqual(average['average_points'], 17.5)
        self.assertEqual(average['average_assists'], 4.0)