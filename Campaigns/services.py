from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.timezone import now
from Contacts.models import ContactList, ContactEmail


def send_campaign_emails(campaign):
    failed_emails = []
    # Log de inicio
    print(f"Enviando emails para la campaña '{campaign.subject}'")

    for contact_list in campaign.contact_lists.all():
        # Log de lista de contactos
        print(f"Procesando lista de contactos: {contact_list.name}")

        # Iterar sobre los contactos relacionados con la lista
        for contact_email in ContactEmail.objects.filter(contact_list=contact_list, is_valid=True):
            # Log de email actual
            print(f"Preparando para enviar a: {contact_email.email}")

            try:
                # Usamos la plantilla HTML para el cuerpo del email
                message = render_to_string('campaign_email.html', {
                    'subject': campaign.subject,
                    'body': campaign.body,
                })

                # Cambiamos a EmailMessage
                email = EmailMessage(
                    campaign.subject,  # Asunto
                    message,  # Cuerpo HTML
                    settings.DEFAULT_FROM_EMAIL,  # Remitente
                    [contact_email.email],  # Destinatario
                )
                email.content_subtype = 'html'  # Especificamos que es HTML
                email.send(fail_silently=False)  # Enviar el email

                # Log de éxito
                print(f"Email enviado exitosamente a: {contact_email.email}")

            except Exception as e:
                # Log de error
                print(f"Error al enviar email a {contact_email.email}: {e}")
                failed_emails.append(contact_email.email)

    # Actualizar el estado de la campaña
    if failed_emails:
        print(f"Fallaron los envíos a los siguientes correos: {failed_emails}")
        campaign.status = 'FAILED'
    else:
        print("Todos los emails se enviaron correctamente.")
        campaign.status = 'SENT'
        campaign.sent_at = now()

    campaign.save()
