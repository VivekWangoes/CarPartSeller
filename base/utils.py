import uuid
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string 
from django.core.mail import EmailMultiAlternatives
from django.utils.http import(urlsafe_base64_encode)
from django.utils.encoding import force_bytes, force_str 
from django.contrib.sites.models import Site
from django.conf import settings
from base.messages import Message

def generate_ref_code():
    code = str(uuid.uuid4()).replace("-","")[:17]
    return code


def send_email_confirmation(form_obj):
    domain = Site.objects.last()
    uid = urlsafe_base64_encode(
                        force_bytes(form_obj.id))
    token = (PasswordResetTokenGenerator()
                .make_token(form_obj))
    context = ({"name": form_obj.first_name,
                "link": f"{domain}/accounts/email-confirmation/{uid}/{token}/"
                })

    email_from = settings.EMAIL_SENDER          
    message = render_to_string(
                        "confirm_email.html", 
                        {'context': context,
                        'domain':domain})
    mail= EmailMultiAlternatives(
    subject = Message.CONFIM_EMAIL,
    body=message,
    from_email=email_from,
    to=[form_obj.email]
    )
    mail.attach_alternative(message, 'text/html')
    mail.send()
