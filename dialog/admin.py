from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.DialogMessage)
class DialogMessageAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'type', 'message', 'created')
    readonly_fields = ('uuid', 'created',)

@admin.register(models.DialogChat)
class DialogChatMessage(admin.ModelAdmin):
    list_display = ('uuid', 'messages')
    readonly_fields = ('uuid', )
