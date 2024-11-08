from django.core.management.base import BaseCommand
from newsletters.models import Mailing

class Command(BaseCommand):
    help = 'Send a mailing'

    def add_arguments(self, parser):
        parser.add_argument('mailing_id', type=int, help='ID of the mailing to send')

    def handle(self, *args, **kwargs):
        mailing_id = kwargs['mailing_id']
        try:
            mailing = Mailing.objects.get(id=mailing_id)
            if mailing.status == 'created':
                mailing.status = 'launched'
                mailing.save()
                self.stdout.write(self.style.SUCCESS('Mailing sent successfully!'))
            else:
                self.stdout.write(self.style.WARNING('Mailing is not in a valid state.'))
        except Mailing.DoesNotExist:
            self.stdout.write(self.style.ERROR('Mailing not found.'))
