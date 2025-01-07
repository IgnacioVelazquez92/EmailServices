from django import forms
from .models import Campaign
from Contacts.models import ContactList


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['subject', 'body', 'contact_lists', 'scheduled_at']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'contact_lists': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'scheduled_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Capturamos el usuario al inicializar
        super().__init__(*args, **kwargs)
        if user:
            # Filtrar listas de contactos según el usuario
            self.fields['contact_lists'].queryset = ContactList.objects.filter(
                user=user)

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject) < 5:
            raise forms.ValidationError(
                "El asunto debe tener al menos 5 caracteres.")
        return subject

    def clean(self):
        """Validación adicional para garantizar integridad."""
        cleaned_data = super().clean()
        contact_lists = cleaned_data.get("contact_lists")
        if contact_lists and not contact_lists.exists():
            raise forms.ValidationError(
                "Debe seleccionar al menos una lista de contactos válida.")
        return cleaned_data
