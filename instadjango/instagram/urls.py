from instagram import views

from django.conf.urls import url

urlpatterns = [
    url(r'^search', views.search, name='search'),
    url(r'^results', views.results, name='results'),
]
