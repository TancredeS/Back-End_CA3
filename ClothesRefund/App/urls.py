from django.urls import path

from . import views
from .views import SignUpView

# This is the URL for the index page.

urlpatterns = [
    path('', views.index, name='index'),
    path('addclothes', views.addclothes, name='addclothes'),
    path('remove_clothes', views.remove_clothes, name='remove_clothes'),
    path('edit_clothes', views.edit_clothes, name='edit_clothes'),
    path('clothes_list', views.clothes_list, name='clothes_list'),
    path("signup/", SignUpView.as_view(), name="signup"),
]