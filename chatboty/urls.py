from django.urls import path

from .views import *

app_name = "chatboty"

urlpatterns = [
    path('chatboty/', ChatterBotAppView.as_view(), name='main'),
    path('api/chatboty/', ChatterBotApiView.as_view(), name='chatboty'),
]