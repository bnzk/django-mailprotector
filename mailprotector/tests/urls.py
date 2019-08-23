"""URLs to run the tests."""
# from compat import patterns, include, url
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^test/$', TemplateView.as_view(template_name='test_app/test.html'), name='test_tag_view'),
    url(r'^admin/', admin.site.urls),
]
