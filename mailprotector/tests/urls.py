"""URLs to run the tests."""
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'test/',
        TemplateView.as_view(template_name='test_app/test.html'),
        name='test_tag_view'
    ),
]
