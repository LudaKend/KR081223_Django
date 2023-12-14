from django.contrib import admin
from spammer.models import Spammer, Client


@admin.register(Spammer)
class SpammerAdmin(admin.ModelAdmin):
    list_display = ('id', 'spammer_name', 'company', 'email', 'is_active')
    list_filter = ('spammer_name', 'is_active',)
    search_fields = ('spammer_name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'email', 'is_active')
    list_filter = ('client_name', 'is_active',)
    search_fields = ('client_name',)

