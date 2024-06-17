import pdb

from random import sample
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, RedirectView
from django.db.models import QuerySet, Max
from django.views.generic.edit import FormView
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login

try:
    from .models import Recipe, User
    from .forms import RegUserForm, AuthUserForm
except ImportError:
    from cook_house.models import Recipe, User
    from cook_house.forms import RegUserForm, AuthUserForm


# Create your views here.

class IndexView(TemplateView):
    sample_max_size = 5
    """5 случайных рецептов"""
    template_name = "cook_house/main.html"

    def get_context_data(self, **kwargs):
        all_recipies: QuerySet = Recipe.objects
        ids = list(all_recipies.values_list('id', flat=True).all())
        context = super().get_context_data(**kwargs)
        actual_sample = self.sample_max_size if len(
            ids) > self.sample_max_size else len(ids)
        try:
            test_5 = sample(ids, k=actual_sample)
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
    """Форма регистрации"""
    form_class = RegUserForm
    template_name = "cook_house/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.validate()
            items = form.clean()
            User.objects.create_user(username=items['login'],
                                     email=items['mail'],
                                     password=items['pwd_first'],
                                     first_name=items['first_name'],
                                     last_name=items['last_name'],
                                     )
            pdb.set_trace(header="cool")
            return redirect('auth')

        else:
            error_hint = ""
            pdb.set_trace(header="invalid")
            form = self.form_class()
            for i in form.errors:
                print(i)
            return render(request, self.template_name,
                          {"form": form, "error_hint": error_hint})


class TestBase(TemplateView):
    template_name = "cook_house/base.html"
    form_name = RegUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pdb.set_trace()
        return context


class AuthUser(FormView):
    """форма авторизации"""
    form_class = AuthUserForm
    template_name = "cook_house/auth.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest, *args, **kwargs):

        form = self.form_class(request.POST)
        try:
            form.validate()
        except ValidationError as e:
            form.errors['login'] = e.message
            return render(request, self.template_name, {"form": form})
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'],
                                password=form.cleaned_data['pwd_first'])
            login(request, user)
            pdb.set_trace(header="valid")
            items = form.clean()
            usr: User = User.objects.filter(username=items['login'])[0]
            name = f"{usr.first_name} {usr.last_name}"
            response = redirect('index')
            response.set_cookie('user', name)

            return response
        else:
            return render(request, self.template_name, {"form": form})


class LogoutUser(View):
    url = "index"

    def get(self, request: HttpRequest, *args, **kwargs):
        response = redirect(self.url)
        pdb.set_trace(header="rdr")
        if response.COOKIES['user']:
            response.COOKIES.pop('user')
        return response
