from django.urls import path
from inscriptions import views
from inscriptions.views import InscriptionCreateView, InscriptionListView, InscriptionUpdateView, InscriptionDetailView, InscriptionDeleteView

app_name = "inscription"

urlpatterns = [
    path('create/',InscriptionCreateView.as_view(),name="create"),
    path('list/',InscriptionListView.as_view(),name="list"),
    path('update/<int:pk>/',InscriptionUpdateView.as_view(),name="update"),
    path('detail/<int:pk>/',InscriptionDetailView.as_view(),name="detail"),
    path('delete/<int:pk>/',InscriptionDeleteView.as_view(),name="delete"),
    path('new/',views.NewInsc,name="new"),

]