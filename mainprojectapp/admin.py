from django.contrib import admin
from .models import comment, user_info

# Register your models here.
admin.site.register(user_info)
admin.site.register(comment)