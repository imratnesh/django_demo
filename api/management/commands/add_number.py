# myapp/management/commands/add_number.py
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Add two numbers."

    def add_arguments(self, parser):
        # Adding commands-line arguments
        parser.add_argument('num1', type=int, help="Number 1")
        parser.add_argument('num2', type=int, help="Number 2")

    def handle(self, *args, **kwargs):
        # Extract arguments python manage.py add_number 3 4
        num1 = kwargs['num1']
        num2 = kwargs['num2']
        # Call the function and display the result
        result = num1 + num2
        self.stdout.write(self.style.SUCCESS(result))
