from django.contrib import admin
from .models import Accessories, Player

# Register your models here.
admin.site.register(Player) # adds model to admin panel

#Accessories model
admin.site.register(Accessories)