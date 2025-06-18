from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="Lav-92326@ya.ru")
        user.set_password("bad54321")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
