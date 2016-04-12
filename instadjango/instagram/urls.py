from instagram import views

from django.conf.urls import url

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^login', views.login, name='login'),
    url(r'^results', views.results, name='results'),
]
