from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/ajax/filter', views.post_form , name='post_form'),
    url(r'detail/(?P<id>[-\w. + ( ) *]+)/$', views.view_detail, name="view_detail"),
]