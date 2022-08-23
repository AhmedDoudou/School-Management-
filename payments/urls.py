from django.urls import path
from . import views 
from .views import PaymentCreateView, PaymentPdfView


app_name = "payment"

urlpatterns = [
    path('list/',views.List,name="list"),
    path('add/',PaymentCreateView.as_view(),name="create"),
        path('pdf/<int:pk>/',PaymentPdfView.as_view(),name="pdf"),
    path('edit/<int:id>',views.Edit,name="update"),
    path('detail/<int:id>',views.Detail,name="detail"),
    path('pay/',views.Pay,name="pay"),
    path('total/',views.Pay,name="total"),
    path('pdf/',views.payment_pdf_view,name="pdf_def"),
    path('total_detail/<int:id>',views.Total,name="total_detail"),






]