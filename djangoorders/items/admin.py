from django.contrib import admin
from .models import Item

class userAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item,userAdmin)
