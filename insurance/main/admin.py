from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(Filial)
admin.site.register(Roles)
admin.site.register(User)
admin.site.register(AutoInshurance)
admin.site.register(HealthInshurance)
admin.site.register(PropertyInshurance)
