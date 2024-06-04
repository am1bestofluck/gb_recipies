import pdb
from random import sample

from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.db.models import QuerySet, Max
from django.views.generic.edit import FormView
try:
    from .models import Recipe
    from .forms import RegUserForm
except ImportError:
    from cook_house.models import Recipe
    from cook_house.forms import RegUserForm

# Create your views here.

class IndexView(TemplateView):
    sample_size = 5
    """5 случайных рецептов"""
    template_name = "cook_house/main.html"

    def get_context_data(self, **kwargs):
        all_recipies: QuerySet = Recipe.objects
        ids = list(all_recipies.values_list('id', flat=True).all())
        context = super().get_context_data(**kwargs)
        # pdb.set_trace()
        try:
            test_5 = sample(ids, k=self.sample_size)
        except ValueError:
            return context
        serve_this = []
        # pdb.set_trace()
        for i in test_5:
            serve_this.append(all_recipies.filter(pk=i)[0])

        context['items'] = serve_this
        # pdb.set_trace()
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


class RegUser(FormView):
    """Форма авторизации"""
    form_class = RegForm
    template_name = "cook_house/register.html"

    def get(self, request, *args, **kwargs):
        pdb.set_trace()
        return request

    def post(self, request, *args, **kwargs):
        pdb.set_trace()
        return request


class TestBase(TemplateView):
    template_name = "cook_house/base.html"
    form_name = RegUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pdb.set_trace()
        return context
