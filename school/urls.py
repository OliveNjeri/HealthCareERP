from django.urls import path 
from . import views

app_name = "school"

urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("admission/", views.admission, name="admission"),
]