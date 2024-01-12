from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'password', 'patronymic', 'date_of_birth', 'position', 'photo', 'st')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(Users, UserAdmin)


class PositionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary')
    list_filter = ('name', 'salary')
    search_fields = ('name', 'salary')


admin.site.register(Positions, PositionsAdmin)




class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')
    list_filter = ('name', 'price', 'quantity')
    search_fields = ('name', 'price', 'quantity')


admin.site.register(Materials, MaterialsAdmin)


class Write_offsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'material', 'quantity', 'date')
    list_filter = ('user', 'material', 'quantity', 'date')
    search_fields = ('user', 'material', 'quantity', 'date')


admin.site.register(Write_offs, Write_offsAdmin)


class PurchasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'material', 'quantity', 'date')
    list_filter = ('user', 'material', 'quantity', 'date')
    search_fields = ('user', 'material', 'quantity', 'date')


admin.site.register(Purchases, PurchasesAdmin)


class Types_of_servicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'master', 'prewiev')
    list_filter = ('name', 'price', 'master', 'prewiev')
    search_fields = ('name', 'price', 'master', 'prewiev')


admin.site.register(Types_of_services, Types_of_servicesAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'material',)
    list_filter = ('name', 'material',)
    search_fields = ('name', 'material',)


admin.site.register(Services, ServicesAdmin)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date', 'types_of_services',)
    list_filter = ('client', 'date', 'types_of_services',)
    search_fields = ('client', 'date', 'types_of_services',)


admin.site.register(Orders, OrdersAdmin)
