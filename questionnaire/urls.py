from django.contrib import admin
from django.urls import path
from questionnaire.views import *

urlpatterns = [
    path('', home),
]
