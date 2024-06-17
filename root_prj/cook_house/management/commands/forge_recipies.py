import pdb

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
try:
    from models import Recipe, CategoryRecipe, User
except ImportError:
    from cook_house.models import Recipe, CategoryRecipe, User
from django.db.models import QuerySet
from random import choice
from pathlib import Path


class Command(BaseCommand):
    help = "Forges arg recipies for each category of dishes"

    def add_arguments(self, parser):
        parser.add_argument("quantity", nargs="+", type=int)

    def handle(self, *args, **options):
        categories: QuerySet = CategoryRecipe.objects.all()
        # pdb.set_trace(header="18")
        for category in categories:
            for repeat in range(options['quantity'][0]):
                title = lorem_ipsum.words(count=3, common=False)
                review = "".join([lorem_ipsum.sentence() for i in range(2)])
                algorythm = "".join(
                    [lorem_ipsum.sentence().capitalize() for i in range(2)])
                time_estimate = choice(range(10, 91, 1))
                preview = choice([i for i in Path(
                    r"C:\reps\gb_recipies\root_prj\cook_house\static\img\default_pics_for_randomizer").iterdir()]).as_posix()
                users:QuerySet = User.objects.all()
                author = choice(users)
                Recipe.objects.create(title=title, review=review,
                                      algorythm=algorythm,
                                      time_estimate=time_estimate,
                                      category=category, preview=preview,
                                      author=author)

