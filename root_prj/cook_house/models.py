import pdb

from django.db import models
from django.utils.translation import gettext_lazy as gtl

DEFAULT_CONTENT = "Soon!"


# Create your models here.
class CategoryRecipe(models.Model):
    class Categories(models.TextChoices):
        SNACKS = "snacks", gtl("Салаты и Закуски")
        FIRST = 'first_dishes', gtl("Супы")
        MAIN = 'main_dishes', gtl("Второе")
        BAKING = 'baking', gtl("Хлеб и Выпечка")
        DESSERTS = 'desserts', gtl("Десерты")
        DRINKS = 'drinks', gtl("Безалкогольные напитки")
        POISON = 'alco', gtl("Пойло")
        SELECT_LATER = 'not_set', gtl("Soon!")

    title = models.CharField(choices=Categories, max_length=20, default=Categories.POISON)
    default_image = models.ImageField(null=True)

    def __str__(self):
        return self.get_title_display()


class Recipe(models.Model):
    title = models.CharField(max_length=100, default=DEFAULT_CONTENT)
    review = models.TextField(blank=False, null=False, db_comment="отсекаем на 100 знаков", default=DEFAULT_CONTENT)
    algorythm = models.TextField(blank=False, null=False, max_length=1000, default=DEFAULT_CONTENT)

    time_estimate = models.IntegerField(blank=False, default=5)
    category = models.ForeignKey('CategoryRecipe', on_delete=models.DO_NOTHING,
                                 default=1)
    preview = models.ImageField(upload_to="dishes", null=True, default=None)
    author = models.CharField(max_length=100, default="Some Cook!")

# class
