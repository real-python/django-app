from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays My custom Mesage'

    def handle(self, *args, **kwargs):
        print("#"*20)
        print("$"*20)
