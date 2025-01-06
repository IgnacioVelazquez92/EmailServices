from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def registro(request):
    if request.method == 'GET':
        return render(request, 'session/register.html', {'form': CustomUserCreationForm()})
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # Validar el formulario automáticamente
            # Guardar el usuario sin persistirlo aún
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()  # Persistir en la base de datos
            login(request, user)  # Autenticar y loguear al usuario
            # Redirigir al usuario al dashboard o página principal
            return redirect('index')
        else:
            # Si el formulario no es válido, mostrar los errores
            return render(request, 'session/register.html', {
                'form': form,
                'mensaje': 'Por favor, corrige los errores en el formulario.'
            })


def index(request):
    return render(request, 'index.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('index')


# def iniciar_sesion(request):
#     if request.method == 'GET':
#         return render(request, 'session/signin.html', {
#             'form': AuthenticationForm(),
#         })
#     else:
#         # Pasar datos directamente al formulario
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('index')
#         # Si el formulario no es válido o la autenticación falla
#         return render(request, 'session/signin.html', {
#             'form': form,
#             'mensaje': 'Usuario o contraseña incorrectos'
#         })

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'session/signin.html', {
            'form': CustomAuthenticationForm(),  # Usamos el formulario personalizado
        })
    else:
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'session/signin.html', {
            'form': form,
            'mensaje': 'Usuario o contraseña incorrectos'
        })
