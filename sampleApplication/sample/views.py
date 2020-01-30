from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, "home.html", {"name": "Mayank"})

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