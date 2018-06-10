from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tables_list, name='tables_list'),
]