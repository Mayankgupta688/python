from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("help", views.help, name="help"),
  path("form", views.form, name="form"),
  path("addNumbers", views.addnumbers, name="addNumbers")
]