from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class ContactList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_lists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class ContactEmail(models.Model):
    email = models.EmailField(max_length=254, validators=[EmailValidator()])
    contact_list = models.ForeignKey(ContactList, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)
    last_sent_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['email', 'contact_list']

    def __str__(self):
        return self.email