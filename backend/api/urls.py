# coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^execute_task/$', views.SendMailApi.as_view(), name='execute_task')
]