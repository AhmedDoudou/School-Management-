from django.urls import path
from parents import views
from parents.views import ParentCreateView, ParentListView, ParentUpdateView, ParentDetailView, ParentDeleteView

app_name = "parent"

urlpatterns = [
    path('create/',ParentCreateView.as_view(),name="create"),
    path('list/',ParentListView.as_view(),name="list"),
    path('update/<int:pk>/',ParentUpdateView.as_view(),name="update"),
    path('detail/<int:pk>/',ParentDetailView.as_view(),name="detail"),
    path('delete/<int:pk>/',ParentDeleteView.as_view(),name="delete"),
]