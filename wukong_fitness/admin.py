from django.contrib import admin

from .models import Equipment, Coach

my_models = [Equipment, Coach]
admin.site.register(my_models)

