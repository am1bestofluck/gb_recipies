from .models import Recipe
from django import forms


class RecipeForm(forms.Form):
    title = forms.CharField(blank=False, null=False, widget=forms.TextInput)
    review = forms.CharField(blank=False, null=False, db_comment="отсекаем на 100 знаков", widget=forms.TextInput)
    algorythm = forms.CharField(blank=False, null=False, max_length=1000, widget=forms.Textarea)
    time_estimate = forms.IntegerField(blank=False, min_value=5, max_value=300, step_size=5)
    preview = forms.ImageField(required=False,)
    author = forms.ChoiceField()