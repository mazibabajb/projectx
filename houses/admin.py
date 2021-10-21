from django.contrib import admin
from .models import *

admin.site.site_header = 'BYORENTALS ADMIN DASHBOARD'
admin.site.register(Property)
admin.site.register(Landload)
admin.site.register(Suburb)

# Register your models here.
