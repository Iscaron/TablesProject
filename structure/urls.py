from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.tables_list, name='tables_list'),
    url(r'^table/(?P<pk>\d+)/$', views.table_detail, name='table_detail'),
    url(r'^table/new/$', views.table_new, name='table_new'),
    url(r'^table/(?P<pk>\d+)/edit/$', views.table_edit, name='table_edit'),
    # url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]