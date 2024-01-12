from django.contrib import admin
from .models import *


class UslugiAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Uslugi, UslugiAdmin)


class NomerAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'cost', 'size', 'count_people', 'count_rooms', 'count_beds', 'photo', 'photo_mini', 'status')
    list_filter = ('name', 'cost', 'size', 'count_people', 'count_rooms', 'count_beds', 'photo', 'photo_mini', 'status')
    search_fields = (
    'name', 'cost', 'size', 'count_people', 'count_rooms', 'count_beds', 'photo', 'photo_mini', 'status')


admin.site.register(Nomer, NomerAdmin)


class SostavUslugiAdmin(admin.ModelAdmin):
    list_display = ('id_uslugi', 'id_nomer')
    list_filter = ('id_uslugi', 'id_nomer')
    search_fields = ('id_uslugi', 'id_nomer')


admin.site.register(SostavUslugi, SostavUslugiAdmin)


class BronAdmin(admin.ModelAdmin):
    list_display = ('id_nomer', 'id_user', 'date_start', 'date_end', 'cost',)
    list_filter = ('id_nomer', 'id_user', 'date_start', 'date_end', 'cost', )
    search_fields = ('id_nomer', 'id_user', 'date_start', 'date_end', 'cost',)


admin.site.register(Bron, BronAdmin)
