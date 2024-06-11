import pdb

from django import forms
from django.core import validators


class RecipeForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    review = forms.CharField(
        widget=forms.TextInput)
    algorythm = forms.CharField(max_length=1000,
                                widget=forms.Textarea)
    time_estimate = forms.IntegerField(min_value=5, max_value=300,
                                       step_size=5)
    preview = forms.ImageField(required=False, )
    author = forms.ChoiceField()


class RegUserForm(forms.Form):
    min_size = 2
    pwd_min_size = 10
    max_size = 50
    login = forms.CharField(
        widget=forms.TextInput)
    mail = forms.EmailField(
        widget=forms.EmailInput)
    first_name = forms.CharField(
        widget=forms.TextInput)
    last_name = forms.CharField(
        widget=forms.TextInput)
    pwd_first = forms.CharField(
        widget=forms.PasswordInput)
    pwd_snd = forms.CharField(
        widget=forms.PasswordInput)

    def validate(self):
        pdb.set_trace(header="check items")


class AuthUserForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput)
    pwd_first = forms.CharField(widget=forms.PasswordInput)
    pwd_second = forms.CharField(widget=forms.PasswordInput)
