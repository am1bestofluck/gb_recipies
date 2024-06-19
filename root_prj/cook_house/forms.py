import pdb

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login

try:
    from .models import User, CategoryRecipe
except ImportError:
    from cookhouse.models import User


class RecipeForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form_main'}))
    review = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form_main'}))
    algorythm = forms.CharField(max_length=1000,
                                widget=forms.Textarea(
                                    attrs={'class': 'form_main'}))
    time_estimate = forms.IntegerField(min_value=5, max_value=300,
                                       step_size=5, widget=forms.NumberInput(
            attrs={'class': 'form_main'}))
    category = forms.ChoiceField(choices=CategoryRecipe.Categories.choices)
    preview = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form_main'}))


class RegUserForm(forms.Form):
    min_size = 2
    pwd_min_size = 10
    max_size = 50
    login = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form_main'}))
    mail = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form_main'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form_main'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form_main'}))
    pwd_first = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form_main'}))
    pwd_snd = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form_main'}))

    def validate(self):
        pdb.set_trace(header="check items#reg")


class AuthUserForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form_main'}),
        label="Логин/почта")
    pwd_first = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form_main'}),
        label="Пароль")

    def validate(self):
        user = authenticate(username=self.data['login'],
                            password=self.data['pwd_first'])
        if not user:
            raise ValidationError("Пользователь не обнаружен")
