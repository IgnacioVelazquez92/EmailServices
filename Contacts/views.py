from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ContactListForm, ContactEmailForm
from django.contrib.auth.decorators import login_required
from .models import ContactList, ContactEmail


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


@login_required
def edit_user(request):
    user = request.user  # Obtener el usuario autenticado

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        try:
            # Actualizar el usuario solo si los datos son válidos y no están en uso
            if User.objects.exclude(pk=user.pk).filter(username=username).exists():
                messages.error(request, "El nombre de usuario ya está en uso.")
            elif User.objects.exclude(pk=user.pk).filter(email=email).exists():
                messages.error(
                    request, "El correo electrónico ya está en uso.")
            else:
                user.username = username
                user.email = email
                user.save()
                messages.success(
                    request, "Tu información fue actualizada correctamente.")
                # Redirige a la página de perfil o a la que elijas
                return redirect("profile")
        except IntegrityError:
            messages.error(
                request, "Ocurrió un error al actualizar tus datos.")

    return render(request, "session/edit_user.html", {"user": user})

# CRUD para ContactList


@login_required()
def contact_list_dashboard(request):
    lists = ContactList.objects.filter(user=request.user)
    return render(request, 'dashboard/contact_list_dashboard.html', {'lists': lists})


@login_required(login_url='/signin/')
def create_contact_list(request):
    if request.method == 'POST':
        form = ContactListForm(request.POST)
        if form.is_valid():
            contact_list = form.save(commit=False)
            contact_list.user = request.user
            contact_list.save()
            return redirect('contact_list_dashboard')
    else:
        form = ContactListForm()
    return render(request, 'dashboard/contact_list_form.html', {'form': form})


@login_required(login_url='/signin/')
def edit_contact_list(request, pk):
    contact_list = get_object_or_404(ContactList, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ContactListForm(request.POST, instance=contact_list)
        if form.is_valid():
            form.save()
            return redirect('contact_list_dashboard')
    else:
        form = ContactListForm(instance=contact_list)
    return render(request, 'dashboard/contact_list_form.html', {'form': form})


@login_required(login_url='/signin/')
def delete_contact_list(request, pk):
    contact_list = get_object_or_404(ContactList, pk=pk, user=request.user)
    if request.method == 'POST':
        contact_list.delete()
        return redirect('contact_list_dashboard')
    return render(request, 'dashboard/contact_list_confirm_delete.html', {'contact_list': contact_list})


# CRUD para ContactEmail

@login_required(login_url='/signin/')
def add_contact_email(request, contact_list_id):
    contact_list = get_object_or_404(
        ContactList, pk=contact_list_id, user=request.user)
    if request.method == 'POST':
        form = ContactEmailForm(request.POST, contact_list=contact_list)
        if form.is_valid():
            email = form.save(commit=False)
            email.contact_list = contact_list
            email.save()
            return redirect('list_detail', pk=contact_list.id)
    else:
        form = ContactEmailForm(contact_list=contact_list)
    return render(request, 'dashboard/contact_email_form.html', {'form': form, 'contact_list': contact_list})


@login_required(login_url='/signin/')
def delete_contact_email(request, email_id):
    email = get_object_or_404(
        ContactEmail, pk=email_id, contact_list__user=request.user)
    if request.method == 'POST':
        email.delete()
        return redirect('contact_list_dashboard')
    return render(request, 'dashboard/contact_email_confirm_delete.html', {'email': email})


@login_required(login_url='/signin/')
def list_detail(request, pk):
    contact_list = get_object_or_404(ContactList, pk=pk, user=request.user)
    emails = ContactEmail.objects.filter(contact_list=contact_list)
    return render(request, 'dashboard/list_detail.html', {
        'contact_list': contact_list,
        'emails': emails
    })
