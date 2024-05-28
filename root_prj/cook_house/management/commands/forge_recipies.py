import pdb

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from cook_house.models import Recipe, CategoryRecipe
from django.db.models import QuerySet
from random import choice


class Command(BaseCommand):
    help = "Forges arg recipies for each category of dishes"

    def add_arguments(self, parser):
        parser.add_argument("quantity", nargs="+", type=int)

    def handle(self, *args, **options):
        categories: QuerySet = Recipe.objects.all()
        pdb.set_trace(header="18")
        for category in categories:
            pdb.set_trace()
            for repeat in options['quantity']:
                title = lorem_ipsum.words(count=3, common=False)
                review = "".join([lorem_ipsum.sentence() for i in range(2)])
                algorythm = "".join([lorem_ipsum.sentence().capitalize() for i in range(2)])
                time_estimate = choice(range(10,91,1))
                category = choice(categories)
                preview = choice([i for i in os.listdir(Path(
                    r"C:\reps\gb_recipies\root_prj\static\img\default_pics_for_randomizer"))])
                author = lorem_ipsum.words(count=2, common=False).title()
                pass
