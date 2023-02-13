from django.contrib import admin
from .models import User

class userAdmin(admin.ModelAdmin):
    pass


admin.site.register(User,userAdmin)
