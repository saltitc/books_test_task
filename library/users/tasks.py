from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


@shared_task
def send_welcome_email(user_id):
    """
    Sends a welcome letter to the user's email
    """
    user = User.objects.get(id=user_id)
    subject = 'Добро пожаловать на наш сайт!'
    message = f'Спасибо, {user.username}, за то что присоединились к нам!'
    from_email = settings.EMAIL_HOST_USER
    to_email = [user.email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email, fail_silently=False)
