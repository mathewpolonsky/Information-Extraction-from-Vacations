from django.contrib import admin
from django.urls import path, include
from .views import AboutView, main_page

urlpatterns = [
    path('', AboutView.as_view(), name="about"),
    path('predict', main_page, name="main")
]