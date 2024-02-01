"""
URL configuration for crowcollector project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crows/', views.crows_index, name="index"),
    path('crows/<int:crow_id>/', views.crows_detail, name='detail'),
    path('crows/create/', views.CrowCreate.as_view(), name='crows_create'),
    path('crows/<int:pk>/update', views.CrowUpdate.as_view(), name='crows_update'),
    path('crows/<int:pk>/delete', views.CrowDelete.as_view(), name='crows_delete'),
    path('crows/<int:crow_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('crows/<int:crow_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
]

