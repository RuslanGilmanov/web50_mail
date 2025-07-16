from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'date_joined')
    ordering = ['date_joined', 'username']


admin.site.register(User, UserAdmin)
