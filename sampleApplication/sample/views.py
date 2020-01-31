from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
import pymongo
from pymongo import MongoClient

import requests

def home(request):
  dest = Destination()
  dest.name = "Delhi"
  return render(request, "home.html", {"name": "Mayank", "dest": dest})

def help(request):
  return render(request, "help.html", {"name": "Mayank"})

def form(request):
  return render(request, "form.html", {"name": "Mayank"})

def addnumbers(request):
  addvalue = int(request.GET["firstNumber"]) + int(request.GET["secondNumber"])
  return render(request, "result.html", {'addvalue': addvalue})

def postaddnumbers(request):
  addvalue = int(request.POST["firstNumber"]) + int(request.POST["secondNumber"])
  return render(request, "result.html", {'addvalue': addvalue})

def postform(request):
  return render(request, "postform.html")

def getemployees(request):

  emplist = []
  emplist = requests.get("http://5c055de56b84ee00137d25a0.mockapi.io/api/v1/employees").json()
  print(emplist)
  return render(request, "getemployees.html", {"emplist": emplist})