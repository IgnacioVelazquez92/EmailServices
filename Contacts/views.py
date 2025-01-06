from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def registro(request):
    if request.method == 'GET':
        return render(request, 'session/register.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except:
                return render(request, 'session/register.html', {
                    'form': UserCreationForm,
                    'mensaje': 'Usuario ya existe'
                })

        return render(request, 'session/register.html', {
            'form': UserCreationForm,
            'mensaje': 'Las contraseñas no coinciden'
        })


def index(request):
    return render(request, 'index.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('index')


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'session/signin.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'session/signin.html', {
                'form': AuthenticationForm,
                'mensaje': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('index')
