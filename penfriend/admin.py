from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'country', 'gender', 'birth_date', 'about_me')
    list_filter = ('country', 'city',  'gender', 'birth_date')

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
