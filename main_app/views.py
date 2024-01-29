from django.shortcuts import render

crows = [
  {'name': 'Bob', 'breed': 'hooded', 'description': 'black and white crow with what looks like a hood', 'age': 2},
  {'name': 'Bucket', 'breed': 'american crow', 'description': 'It looks much like other all-black corvids. They are very intelligent, and adaptable to human environments.', 'age': 0},
]

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def crows_index(request):
  return render(request, 'crows/index.html', {
    'crows': crows,
  })