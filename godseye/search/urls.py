from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.index, name="index"),
    path("find", views.find, name="find"),
    path("imgfind", views.imgfind, name="imgfind"),
    path("searchimage", views.searchimage, name="searchimage"),
    path("search_json", views.search_json, name="search_json"),
]
