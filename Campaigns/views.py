from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CampaignForm
from .models import Campaign
from django.core.mail import send_mail
from django.conf import settings
from .services import send_campaign_emails
from django.utils import timezone
from django.template.loader import render_to_string
from Contacts.models import ContactList, ContactEmail


@login_required
def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, user=request.user)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            form.save_m2m()  # Guarda la relación con las listas de contactos
            return redirect('campaign_list')
    else:
        form = CampaignForm(user=request.user)  # Pasar el usuario actual
    return render(request, 'create_campaign.html', {'form': form})


@login_required
def send_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id, user=request.user)
    send_campaign_emails(campaign)
    return redirect('campaign_list')


@login_required
def campaign_list(request):
    campaigns = Campaign.objects.filter(user=request.user)
    return render(request, 'campaign_list.html', {'campaigns': campaigns})


@login_required
def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id, user=request.user)
    return render(request, 'campaign_detail.html', {'campaign': campaign})


@login_required
def edit_campaign(request, pk):
    # Asegurarnos de que solo se pueda acceder a campañas del usuario actual
    campaign = get_object_or_404(Campaign, pk=pk, user=request.user)

    if request.method == 'POST':
        # Pasar el usuario actual al formulario para filtrar correctamente las listas de contactos
        form = CampaignForm(request.POST, instance=campaign, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('campaign_list')
    else:
        # Pasar el usuario al formulario al cargar la instancia existente
        form = CampaignForm(instance=campaign, user=request.user)

    return render(request, 'edit_campaign.html', {'form': form})


@login_required
def delete_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id, user=request.user)
    campaign.delete()
    return redirect('campaign_list')


def send_test_email():
    send_mail(
        'Asunto de prueba',  # Asunto del correo
        'Este es el cuerpo del correo',  # Cuerpo del correo
        settings.DEFAULT_FROM_EMAIL,  # Correo de envío
        ['destinatario@example.com'],  # Dirección de destino
        fail_silently=False,  # Si hay un error, se lanza una excepción
    )
