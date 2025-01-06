from django.contrib import admin
from .models import ContactList, ContactEmail

admin.site.register(ContactList)
admin.site.register(ContactEmail)