from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^mapdemo/$', views.mapdemo, name="mapdemo"),
	url(r'^mapdemo2/$', views.mapdemo2, name="mapdemo2"),
	url(r'^mapdemo3/$', views.mapdemo3, name="mapdemo3"),
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
]