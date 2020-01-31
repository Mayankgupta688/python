from django.urls import path

from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("help", views.help, name="help"),
  path("form", views.form, name="form"),
  path("addNumbers", views.addnumbers, name="addNumbers"),
  path("postform", views.postform, name="postform"),
  path("postaddnumbers", views.postaddnumbers, name="postaddnumbers"),
  path("getemployees", views.getemployees, name="getemployees")
]