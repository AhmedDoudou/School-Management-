from django.urls import path
from . import views
from .views import DashbordView, Login

# app_name = "core"

urlpatterns = [
    path('',Login.as_view(),name="login"),
    path('dashboard/',DashbordView.as_view(),name="dashboard")

]
