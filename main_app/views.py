from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class CrowCreate (CreateView):
  model = Crow
  fields = '__all__'
  success_url = '/crows/{id}'

class CrowUpdate(UpdateView):
  model = Crow
  fields = ['breed', 'description', 'age']

class CrowDelete(DeleteView):
  model = Crow
  success_url = '/crows'