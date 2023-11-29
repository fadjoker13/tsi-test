from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tsi.views import PlayersList

router = routers.SimpleRouter()
router.register('players', PlayersList, basename='players')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/', include(router.urls)),    
]
