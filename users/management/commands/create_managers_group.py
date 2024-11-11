from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from newsletters.models import Mailing, Message, Client

class Command(BaseCommand):
    help = 'Create the Managers group and assign permissions'

    def handle(self, *args, **kwargs):
        managers_group, created = Group.objects.get_or_create(name='Managers')
        if created:
            self.stdout.write("Managers group created.")

        permissions = Permission.objects.filter(
            content_type__model__in=['mailing', 'message', 'client']
        )
        managers_group.permissions.set(permissions)
        managers_group.save()

        self.stdout.write("Permissions assigned to Managers group.")
