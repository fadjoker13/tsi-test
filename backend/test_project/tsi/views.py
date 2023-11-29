from django.shortcuts import render
from .models import Player
from rest_framework.viewsets import ModelViewSet
from .serializers import PlayersSerializer
from rest_framework.response import Response

def dashboard(request):
   return render(request)

class PlayersList(ModelViewSet):
    #queryset = Player.objects.all()
    serializer_class = PlayersSerializer

    def get_queryset(self):
        return Player.objects.all()
    
