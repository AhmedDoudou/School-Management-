from django.urls import path
from programs import views
from programs.views import ProgramCreateView, ProgramListView, ProgramUpdateView, ProgramDetailView, ProgramDeleteView

app_name = "program"

urlpatterns = [
    path('create/',ProgramCreateView.as_view(),name="create"),
    path('list/',ProgramListView.as_view(),name="list"),
    path('update/<int:pk>/',ProgramUpdateView.as_view(),name="update"),
    path('detail/<int:pk>/',ProgramDetailView.as_view(),name="detail"),
    path('delete/<int:pk>/',ProgramDeleteView.as_view(),name="delete"),
]