from rest_framework import serializers
from rest_framework import generics
from .models import Player

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
    
    def validate(self, attrs):
        name_player = attrs.get('name')
        for i in name_player:
            if not i.isalnum() and i != ' ':
                raise serializers.ValidationError('Name must contain only letters')
        return attrs

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayersSerializer