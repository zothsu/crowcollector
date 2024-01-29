from django.shortcuts import render
from .models import Crow

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def crows_index(request):
  crows = Crow.objects.all()
  return render(request, 'crows/index.html', {'crows': crows })

def crows_detail(request, crow_id):
  crow = Crow.objects.get(id=crow_id)
  return render(request, 'crows/detail.html', { 'crow': crow })