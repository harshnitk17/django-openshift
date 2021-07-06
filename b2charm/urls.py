from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/ajax/filter', views.post_form , name='post_form')
]