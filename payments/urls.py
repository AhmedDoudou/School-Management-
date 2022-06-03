from django.urls import path
from . import views 


app_name = "payment"

urlpatterns = [
    path('list/',views.List,name="list"),
    path('add/',views.Add,name="create"),
    path('edit/<int:id>',views.Edit,name="update"),
    path('pay/',views.Pay,name="pay"),
    path('total/',views.Pay,name="total"),




]