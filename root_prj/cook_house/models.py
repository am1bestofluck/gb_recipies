import pdb

from django.db import models
from django.utils.translation import gettext_lazy as gtl


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    review = models.TextField(blank=False, null=False,db_comment="отсекаем на 100 знаков" )
    algorythm = models.TextField(blank=False, null=False, max_length=1000)
    time_estimate = models.IntegerField(blank=False,)
    preview = models.ImageField()
    author = models.ForeignKey('Users', editable=False)


class CategoryRecipe(models.Model):
    class Categories(models.TextChoices):
        SNACKS = "snacks", gtl("Салаты и Закуски")
        FIRST = 'first_dishes', gtl("Супы")
        MAIN = 'main_dishes', gtl("Второе")
        BAKING = 'baking', gtl("Хлеб и Выпечка")
        DESSERTS = 'desserts', gtl("Десерты")
        DRINKS = 'drinks', gtl("Безалкогольные напитки")
        POISON = 'alco', gtl("Пойло")

    title = models.CharField(choices=Categories, max_length=20)
    default_image = models.ImageField(null=True)

    def __str__(self):
        return self.get_title_display()
# class
