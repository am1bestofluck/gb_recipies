import pdb
from dataclasses import dataclass
from django.db import models
from django.utils.translation import gettext_lazy as gtl
from pathlib import Path
from PIL import Image

DEFAULT_CONTENT = "Soon!"


# Create your models here.
class CategoryRecipe(models.Model):
    IMAGE_SIZE = 640, 360,

    class Categories(models.TextChoices):
        SNACKS = "snacks", gtl("Салаты и Закуски")
        FIRST = 'first_dishes', gtl("Супы")
        MAIN = 'main_dishes', gtl("Второе")
        BAKING = 'baking', gtl("Хлеб и Выпечка")
        DESSERTS = 'desserts', gtl("Десерты")
        DRINKS = 'drinks', gtl("Безалкогольные напитки")
        POISON = 'alco', gtl("Пойло")
        SELECT_LATER = 'not_set', gtl("Soon!")

    @dataclass
    class DefaultPicture:
        title: str
        img: Path


    @staticmethod
    def resize():
        """Масштабирует дефолтные картинки до 640*360"""
        for i in Path.iterdir("static\\img\\default_categories"):
            a = Image.open(i)
            a = a.resize(IMAGE_SIZE)
            a.save(i)
        return True

    default_pictures: dict[Categories, Path] = {
        Categories.SNACKS: Path("static\\img\\default_categories\\snacks.jpg"),
        Categories.FIRST: Path("static\\img\\default_categories\\first.jpg"),
        Categories.MAIN: Path("static\\img\\default_categories\\main.jpg"),
        Categories.BAKING: Path("static\\img\\default_categories\\baking.jpg"),
        Categories.DESSERTS: Path(
            "static\\img\\default_categories\\desserts.jpg"),
        Categories.DRINKS: Path("static\\img\\default_categories\\drinks.jpg"),
        Categories.POISON: Path("static\\img\\default_categories\\poison.jpg"),
        Categories.SELECT_LATER: Path(
            "static\\img\\default_categories\\noway.jpg"),

    }

    title = models.CharField(choices=Categories, max_length=20,
                             default=Categories.POISON)
    default_image = models.ImageField(null=True)

    def __str__(self):
        return self.get_title_display()


class Recipe(models.Model):
    title = models.CharField(max_length=100, default=DEFAULT_CONTENT)
    review = models.TextField(blank=False, null=False,
                              db_comment="отсекаем на 100 знаков",
                              default=DEFAULT_CONTENT)
    algorythm = models.TextField(blank=False, null=False, max_length=1000,
                                 default=DEFAULT_CONTENT)

    time_estimate = models.IntegerField(blank=False, default=5)
    category = models.ForeignKey('CategoryRecipe', on_delete=models.DO_NOTHING,
                                 default=1)
    preview = models.ImageField(upload_to="dishes", null=True, default=None)
    author = models.CharField(max_length=100, default="Some Cook!")

# class
if __name__ == '__main__':
    CategoryRecipe.resize()
