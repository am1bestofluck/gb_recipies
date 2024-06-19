from .views import IndexView, CreateView, RecipeViewRUD, TestBase, RegUser, \
    AuthUser,LogoutUser,PersonOwnRecipies
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('new_cook', RegUser.as_view(), name='new_cook'),
    path('auth', AuthUser.as_view(), name="auth"),
    path('logout', LogoutUser.as_view(),name="logout"),
    path('', IndexView.as_view(), name='index'),
    path('create_r', CreateView.as_view(), name='create_r'),
    path('focus_r/<int:id>', RecipeViewRUD.as_view(), name='focus_r'),
    path('test_base', TestBase.as_view(), name="test_base"),
    path('creations',PersonOwnRecipies.as_view(),name="creations"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
