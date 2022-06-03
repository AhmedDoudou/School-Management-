from django.urls import path
from studentManagement import views 
from studentManagement.views import (
    StudentCreateView,BlanckView,
    StudentListView, StudentUpdateView, 
    StudentDetailView, StudentDeleteView,
    StudentPdfView,ChartView,StudentsPdfView
     )

app_name = "student"

urlpatterns = [
    path('create/',StudentCreateView.as_view(),name="create"),
    path('list/',StudentListView.as_view(),name="list"),
    path('update/<int:pk>/',StudentUpdateView.as_view(),name="update"),
    path('edit/<int:id>/',views.Edit,name="edit"),
    path('detail/<int:id>/',views.Detail,name="detail"),
    # path('detail/<int:pk>/',StudentDetailView.as_view(),name="detail"),
    path('delete/<int:pk>/',StudentDeleteView.as_view(),name="delete"),
    path('pdf/<int:pk>/',StudentPdfView.as_view(),name="pdf"),
    path('list/pdf/',StudentsPdfView.as_view(),name="list_pdf"),
    path('blanck/',BlanckView.as_view(),name="blanck"),
    path('chart/',ChartView.as_view(),name="chart"),
    path('newinscription/',views.NewInscription,name="newinscription"),

]
