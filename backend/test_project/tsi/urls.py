from django.urls import path
from . import views
from .views import PlayersList
from .serializers import PlayerDetail


urlpatterns = [
    path('players', PlayersList.as_view(), name='players-list'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
]
