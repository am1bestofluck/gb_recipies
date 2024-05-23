import pdb

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = "Forges arg recipies for each category of dishes"

    def add_arguments(self, parser):
        parser.add_argument("quantity", nargs="+", type=int)

    @staticmethod
    def collect_categories() -> List[str]:
        return []

    def handle(self, *args, **options):
        todo = self.collect_categories()
        for category in todo:
            for repeat in options['quantity']:
                pdb.set_trace()


