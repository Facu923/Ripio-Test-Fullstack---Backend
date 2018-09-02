from django.contrib import admin
from backend.api.models import Client, \
    CurrencyType, Account, Transfer

admin.site.register(Client)
admin.site.register(CurrencyType)
admin.site.register(Account)
admin.site.register(Transfer)
