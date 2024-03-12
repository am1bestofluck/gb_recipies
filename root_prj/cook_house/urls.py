from .views import IndexView, CreateView, RecipeViewRUD
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_r', CreateView.as_view(), name='create_r'),
    path('focus_r/<int:id>', RecipeViewRUD.as_view(), name='focus_r'),
]
