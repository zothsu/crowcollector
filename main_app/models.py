from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=50)

class Crow(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'crow.id': self.id})

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
  # Create a FK for crow_id
  crow = models.ForeignKey(Crow, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']