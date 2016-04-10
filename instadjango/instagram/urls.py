from instagram import views

from django.conf.urls import url

urlpatterns = [
    url(r'^search', views.search, name='search'),
    url(r'^login', views.login, name='login'),
    url(r'', views.index, name='index'),
]
