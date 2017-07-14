from django.conf.urls import url
from django.contrib import admin

from tden1 import views

urlpatterns = [
    url(r"deneme_url2$" ,views.deneme2)
]
