from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    jersey_num = models.IntegerField()
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name
