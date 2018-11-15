from django.urls import path
from Registration import views

urlpatterns = [
    path('', views.Register,name="Register page"), 
]
