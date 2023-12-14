from django.contrib import admin
from spammer.models import Spammer


@admin.register(Spammer)
class SpammerAdmin(admin.ModelAdmin):
    list_display = ('id', 'spammer_name', 'company', 'email', 'is_active')
    list_filter = ('spammer_name', 'is_active',)
    search_fields = ('spammer_name',)
