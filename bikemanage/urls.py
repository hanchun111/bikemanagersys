from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user/$', views.show_user),
    url(r'^bikes/$',views.show_bikes),
    url(r'^bike/$',views.show_bike),
    url(r'^add_user/$', views.add_user),
    url(r'^add_bike/$',views.add_bike),
    url(r'^update_bike_status/$', views.update_bike_status),
    url(r'^update_user/$',views.update_user),
]