from django.contrib import admin

from profiles_api import models

# Register your models here.
"""Registering model will let model to appear under django administration view"""
admin.site.register(models.UserProfile)
