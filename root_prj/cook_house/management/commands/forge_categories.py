import pdb

from django.core.management.base import BaseCommand

try:
    from models import CategoryRecipe, Recipe
except ImportError:
    from cook_house.models import CategoryRecipe, Recipe
from django.db.models import QuerySet


class Command(BaseCommand):
    help = "Forges arg recipies for each category of dishes"

    def handle(self, *args, **options):
        existing_categories: QuerySet = CategoryRecipe.objects.all()
        # pdb.set_trace()
        if existing_categories:
            self.stdout.write(
                "Можно создавать категории по умолчанию только если их вообще нет\n")
            return None
        else:
            # CategoryRecipe.resize()
            # pdb.set_trace(header="!")
            for new_item in CategoryRecipe.Categories.__members__.items():
                pdb.set_trace(header="forge_categories")
                CategoryRecipe.objects.create(title=new_item[1],default_image=CategoryRecipe.default_pictures[new_item[1]])
