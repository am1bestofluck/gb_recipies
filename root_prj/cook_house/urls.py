from .views import IndexView, CreateView, RecipeViewRUD, TestBase, RegUser
from django.urls import path

urlpatterns = [
    path('new_cook', RegUser.as_view(), name='new_cook'),
    path('', IndexView.as_view(), name='index'),
    path('create_r', CreateView.as_view(), name='create_r'),
    path('focus_r/<int:id>', RecipeViewRUD.as_view(), name='focus_r'),
    path('test_base', TestBase.as_view(), name="test_base"),
]
