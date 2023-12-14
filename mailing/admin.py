from django.contrib import admin
from mailing.models import Mailing, Period, StatusMailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'spammer', 'time', 'period', 'status')
    list_filter = ('spammer', 'time', 'status',)
    search_fields = ('subject', 'spammer', 'time', 'period',)


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'period')
    list_filter = ('period',)
    search_fields = ('period',)

@admin.register(StatusMailing)
class StatusMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_filter = ('status',)
    search_fields = ('status',)

