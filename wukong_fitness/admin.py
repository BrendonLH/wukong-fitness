from django.contrib import admin

from .models import Equipment, Coaches

my_models = [Equipment, Coaches]
admin.site.register(my_models)

