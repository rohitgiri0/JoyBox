from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def handle_user_signed_up(request, sociallogin, user, **kwargs):
    new_user_data=sociallogin.account.extra_data
    print(new_user_data)


