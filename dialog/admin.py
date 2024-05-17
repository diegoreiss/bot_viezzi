from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.DialogMessage)
admin.site.register(models.DialogChat)
