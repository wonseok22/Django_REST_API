from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from dataTest import views
# Serializers define the API representation.

urlpatterns = [
    path('users/', views.user_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]