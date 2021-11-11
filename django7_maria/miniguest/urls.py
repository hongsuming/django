from django.urls import path
from miniguest import views

urlpatterns = [
    path('', views.listFunc), 
    path('insert/', views.insertFunc), 
    path('submit/', views.submitFunc), 
    path('delete/', views.deleteFunc),  
] 