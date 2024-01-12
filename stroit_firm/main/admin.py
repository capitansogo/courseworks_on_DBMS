from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'password', 'patronymic', 'phone', 'warehouse_manager', 'cashier')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)


class SubtypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Subtypes, SubtypesAdmin)


class TypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Types, TypesAdmin)


class Subtype_TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'subtype')
    list_filter = ('type', 'subtype')
    search_fields = ('type', 'subtype')


admin.site.register(Subtype_Type, Subtype_TypeAdmin)


class ManufacturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'street', 'house', 'phone')
    list_filter = ('name', 'city', 'street', 'house', 'phone')
    search_fields = ('name', 'city', 'street', 'house', 'phone')


admin.site.register(Manufacturers, ManufacturesAdmin)


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'manufacturer', 'unit_of_measurement', 'price', 'price_delivery', 'photo')
    list_filter = ('name', 'type', 'manufacturer', 'unit_of_measurement', 'price', 'price_delivery', 'photo')
    search_fields = ('name', 'type', 'manufacturer', 'unit_of_measurement', 'price', 'price_delivery', 'photo')


admin.site.register(Materials, MaterialsAdmin)



class ShopsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'street', 'house')
    list_filter = ('name', 'city', 'street', 'house')
    search_fields = ('name', 'city', 'street', 'house')


admin.site.register(Shops, ShopsAdmin)


class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'sostav_prodazhi', 'user')
    list_filter = ('date', 'sostav_prodazhi', 'user')
    search_fields = ('date', 'sostav_prodazhi', 'user')


admin.site.register(Sales, SalesAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'material', 'quantity', 'total_cost')
    list_filter = ('material', 'quantity', 'total_cost')
    search_fields = ('material', 'quantity', 'total_cost')


admin.site.register(Cart, CartAdmin)
