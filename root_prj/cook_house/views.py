import pdb

from random import sample
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, RedirectView
from django.db.models import QuerySet, Max
from django.views.generic.edit import FormView
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout

try:
    from .models import Recipe, User, CategoryRecipe
    from .forms import RegUserForm, AuthUserForm, RecipeForm
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
        # pdb.set_trace(header="users")
        return context


class PersonOwnRecipies(TemplateView):
    template_name = "cook_house/proprietory.html"

    def get_context_data(self, **kwargs):
        user_ = self.request.user.id
        all_recipies: QuerySet = Recipe.objects.filter(
            author=self.request.user.id)
        # pdb.set_trace(header="personalized")
        context = super().get_context_data(**kwargs)
        context['items'] = all_recipies
        return context


class ItemView(TemplateView):
    """один рецепт, детально"""
    template_name = "cook_house/templates/cook_house/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateView(TemplateView):
    template_name = "cook_house/add_recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeForm()
        return context

    @staticmethod
    def return_Category(value: str) -> CategoryRecipe:
        blank_id = 8
        for i in CategoryRecipe.objects.all():
            if i.get_title_display() == value:
                return i
            return CategoryRecipe.objects.filter(pk=blank_id).first()

    def post(self, request, *args, **kwargs):
        pdb.set_trace()
        form = RecipeForm(self.request.POST)

        if form.is_valid():
            items = form.clean()
            author_ = request.user
            # pdb.set_trace(header="create")
            Recipe.objects.create(
                title=items['title'],
                review=items['review'],
                algorythm=items['algorythm'],
                time_estimate=items['time_estimate'],
                category=self.return_Category(items['category']),
                preview=items['preview'],
                author=author_
            )
            return HttpResponse("ok!")
        else:
            error_hint = ""
            # pdb.set_trace(header="invalid")
            form = self.form_class()
            return render(request, self.template_name,
                          {"form": form, "error_hint": error_hint})


class RecipeViewRUD(TemplateView):
    """Посмотреть рецепт """
    template_name = "cook_house/specific.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Recipe.objects.filter(pk=kwargs['id']).first()
        return context


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
            # pdb.set_trace(header="cool")
            return redirect('auth')

        else:
            error_hint = ""
            # pdb.set_trace(header="invalid")
            form = self.form_class()
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
            # pdb.set_trace(header="valid")
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
        logout(request)
        return redirect(self.url)
