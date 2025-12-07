from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")
def add(request):
    return render(request, "student/add_student.html")
def all(request):
    return render(request, "student/all_student.html")
