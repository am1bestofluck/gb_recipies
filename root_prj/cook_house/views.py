import pdb

from django.shortcuts import render
from django.views.generic import TemplateView, View


# Create your views here.

class IndexView(TemplateView):
    """5 случайных рецептов"""
    template_name = "cook_house/main.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ItemView(TemplateView):
    """один рецепт, детально"""
    template_name = "cook_house/templates/cook_house/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateView(TemplateView):
    template_name = "cook_house/recipe_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RecipeViewRUD(View):
    """Добавляем/редактируем рецепт """
    template_name = "cook_house/recipe_edit.html"

    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass


class RegUser(View):
    """Форма авторизации"""

    def get(self):
        pass

    def post(self):
        pass


class TestBase(TemplateView):
    template_name = "cook_house/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pdb.set_trace()
        return context
