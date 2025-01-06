from django.db import models
from django.contrib.auth.models import User
from Contacts.models import ContactList

class Campaign(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Borrador'),
        ('SCHEDULED', 'Programada'),
        ('SENDING', 'Enviando'),
        ('SENT', 'Enviada'),
        ('FAILED', 'Fallida'),
    ]

    subject = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campaigns')
    contact_lists = models.ManyToManyField(ContactList, related_name='campaigns')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.subject} - {self.status}"