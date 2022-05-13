"""URLs to run the tests."""
# from compat import patterns, include, url
from django.urls import re_path
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    re_path(r'^test/$', TemplateView.as_view(template_name='test_app/test.html'), name='test_tag_view'),
    re_path(r'^admin/', admin.site.urls),
]
