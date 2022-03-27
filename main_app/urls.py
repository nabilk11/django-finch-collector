from unicodedata import name
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
   # player delete path
   path('players/<int:pk>/delete', views.PlayerDelete.as_view(), name="player_delete"),

   #User PF Path
   path('user/<username>/', views.profile, name='profile'),

   #Accessories PATHS
   path('accessories/', views.accessories_index, name='accessories_index'),
   path('accessories/<int:accessories_id>', views.accessories_show, name='accessories_show'),
   path('accessories/create', views.AddAccessory.as_view(), name='add_accessory'),
   path('accessories/<int:pk>/update', views.UpdateAccessory.as_view(), name='update_accessory'),
   path('accessories/<int:pk>/delete', views.DeleteAccessory.as_view(), name='delete_accessory'),


]