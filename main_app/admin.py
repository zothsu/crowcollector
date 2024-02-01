from django.contrib import admin
from .models import Crow, Feeding, Toy

# Register your models here.
admin.site.register(Crow)
admin.site.register(Feeding)
admin.site.register(Toy)