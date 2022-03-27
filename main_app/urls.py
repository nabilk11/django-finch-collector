from django.urls import path, include
from . import views

# this like app.use() in express
urlpatterns = [
   path('', views.Home.as_view(), name="Home"),
   path('about/', views.About.as_view(), name="about"),
   # players list path
   path('players/', views.PlayersList.as_view(), name="players"),
   # add a player path
   path('players/new/', views.Add_Player.as_view(), name="add_player"),
   # player detail path
   path('players/<int:pk>/', views.PlayerDetail.as_view(), name="player_detail"),
   # player update path
   path('players/<int:pk>/update', views.PlayerUpdate.as_view(), name="player_update"),
]