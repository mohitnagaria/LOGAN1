from django.conf.urls import url
from django.contrib import admin
from .views import(
	post_list,
	post_home,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	url(r'^$', post_home),
	url(r'^list/$', post_list),
	url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
	url(r'^update/$', post_update),
	url(r'^delete/$', post_delete),
]