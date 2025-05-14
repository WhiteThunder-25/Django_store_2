from django.urls import path
from django.utils.translation.trans_real import catalog

from . import views


app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    ]
