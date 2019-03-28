from django.contrib import admin
from django.urls import path
from pyquestionnaire.views import *

urlpatterns = [
    path('', home),
    path('data/', handle_form_data),
]
