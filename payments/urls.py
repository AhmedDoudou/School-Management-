from django.urls import path
from . import views 


app_name = "payment"

urlpatterns = [
    path('list/',views.List,name="list"),
    path('add/',views.Add,name="add"),

]