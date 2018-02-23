from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView

from firstapp import views

urlpatterns = [
    path('', views.index),
    path('about/', TemplateView.as_view(template_name="about.html",
        extra_context={"header": "О сайте"})),
    path('contact/', TemplateView.as_view(template_name="contact.html")),
    path('details/', views.details),
    path('home/', TemplateView.as_view(template_name="home.html")),
    path('more/', TemplateView.as_view(template_name="more_about.html")),
]

