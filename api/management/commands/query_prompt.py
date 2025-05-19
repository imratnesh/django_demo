# myapp/management/commands/add_number.py
from django.core.management.base import BaseCommand

from api.utils import get_answer


class Command(BaseCommand):
    help = "Get query and answer."

    def add_arguments(self, parser):
        # Adding commands-line arguments
        parser.add_argument('query', type=str, help="query")

    def handle(self, *args, **kwargs):
        # Extract arguments
        query = kwargs['query']
        # Call the function and display the result
        result = get_answer(query)
        self.stdout.write(self.style.SUCCESS(result))
