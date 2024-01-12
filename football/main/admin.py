from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(League)
admin.site.register(Teams)
admin.site.register(Players)
admin.site.register(Coach)
admin.site.register(Matches)
admin.site.register(WinnersChampions)
admin.site.register(WinnersEurope)
