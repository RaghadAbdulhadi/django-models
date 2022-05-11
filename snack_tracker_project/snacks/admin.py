from django.contrib import admin
from .models import Snack
# Register your models here.

# class AdminThing(admin.ModelAdmin):
#     pass

admin.site.register(Snack)