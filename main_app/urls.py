from unicodedata import name
from django.urls import path, include
from . import views

# this like app.use() in express
urlpatterns = [
   path('', views.Home.as_view(), name="Home"),
   path('about/', views.About.as_view(), name="about"),
   path('teams/', views.Teams.as_view(), name="Teams")

]