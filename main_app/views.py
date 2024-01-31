from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Crow
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'crows/detail.html', { 'crow': crow, 'feeding_form': feeding_form })

def add_feeding(request, crow_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the crow_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.crow_id = crow_id
    new_feeding.save()
  return redirect('detail', crow_id=crow_id)

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