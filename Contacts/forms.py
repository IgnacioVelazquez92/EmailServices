from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ContactList, ContactEmail


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Correo Electrónico",
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingresa tu correo electrónico'})
    )
    first_name = forms.CharField(
        required=True,
        label="Nombre",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'})
    )
    last_name = forms.CharField(
        required=True,
        label="Apellido",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ingresa tu apellido'})
    )
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Crea tu nombre de usuario'})
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Crea una contraseña segura'})
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirma tu contraseña'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu usuario',
        }),
        label="Usuario"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu contraseña',
        }),
        label="Contraseña"
    )


class ContactListForm(forms.ModelForm):
    class Meta:
        model = ContactList
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la lista'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la lista',
                'rows': 3,
            }),
        }


class ContactEmailForm(forms.ModelForm):
    class Meta:
        model = ContactEmail
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del contacto'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
            })
        }

    def __init__(self, *args, **kwargs):
        self.contact_list = kwargs.pop('contact_list', None)
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and self.contact_list:
            if ContactEmail.objects.filter(email=email, contact_list=self.contact_list).exists():
                raise forms.ValidationError(
                    'Este email ya existe en esta lista de contactos')
        return email
