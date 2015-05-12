from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/', views.product, name='product'),
    url(r'^tickets/', views.tickets, name='tickets'),
]
