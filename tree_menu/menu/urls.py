from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    re_path(r'^(?P<url>.+)/$', views.dynamic_menu_view, name='dynamic_menu'),
]