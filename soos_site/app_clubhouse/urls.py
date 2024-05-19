from django.urls import path
from .views import (
    clubhouse_home,
    mancala, dotsandboxes
)

urlpatterns = [
    path('', clubhouse_home, name='clubhouse_home'),
    path('mancala/', mancala, name='mancala'),
    path('dotsandboxes/', dotsandboxes, name='dotsandboxes')
]
