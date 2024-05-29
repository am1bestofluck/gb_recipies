from django.contrib import admin

# Register your models here.
from .models import CategoryRecipe, Recipe, User

from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)

@admin.register(CategoryRecipe)
class CategoryRecipeAdmin(admin.ModelAdmin):
    list_display = ("pk","title")
    ordering = ["pk","title"]
    list_filter = ["title"]
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
