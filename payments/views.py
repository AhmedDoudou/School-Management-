from django.http import HttpResponse
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from core.models import Abonnement, Payment, Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django_xhtml2pdf.views import PdfMixin
from django.views.generic import CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PaymentForm
from django.template.loader import get_template
from django_xhtml2pdf.utils import generate_pdf
from xhtml2pdf import pisa
from django.core.files.storage import FileSystemStorage

def List(req):
    payments = Payment.objects.all()
    context = {"payments":payments}
    return render(req, "payment/list.html",context)


class PaymentCreateView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    template_name = "payment/add.html/"
    model = Payment
    fields = ("__all__")
    success_url = reverse_lazy('payment:pdf')
    success_message = "The Payment Created successfully "
    def get_context_data(self, **kwargs):
        context = super(PaymentCreateView,self).get_context_data(**kwargs)
        page_title = 'Add Payment'
        context.update({
            "page_title":page_title
         })
        return context
    

def Add(req):
    form = PaymentForm
    if req.method =="POST":
        form = PaymentForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            redirect("payment:pdf")
        else:
            form = PaymentForm()
    context = {"form":form}
    return render(req, "payment/add.html",context)


def Edit(req,id):
    payment = Payment.objects.get(id=id)
    form = PaymentForm(instance=payment)
    if req.method =="POST":
        form = PaymentForm(req.POST,req.FILES,instance=payment)
        if form.is_valid():
            form.save()
            return redirect("payment:list")
    context ={
        "form":form
    }
    return render(req,"payment/edit.html",context)


def Pay(req):
    students = Student.objects.all()
    abonnements = Abonnement.objects.all()
    if req.method =="POST" and req.FILES['cheque_file']:
        student_id = req.POST.get("student")
        abonnement_id = req.POST.get("abonnement")
        pay_method = req.POST.get("pay_method")
        pay_by = req.POST.get("pay_by")
        student = Student.objects.get(id=student_id)
        abonnement = Abonnement.objects.get(id=abonnement_id)
        # SHEQUE FILE 
        cheque_file = req.FILES['cheque_file']
        fs = FileSystemStorage()
        cheque_file = fs.save(cheque_file.name, cheque_file)
        uploaded_file_url = fs.url(cheque_file)
        # CREATE PAYMENT if SHEQUE
        payment = Payment (student = student,abonnement=abonnement,payment_method=pay_method,created_by=pay_by, picture=uploaded_file_url)
            
    if req.method =="POST":
        student_id = req.POST.get("student")
        abonnement_id = req.POST.get("abonnement")
        pay_method = req.POST.get("pay_method")
        pay_by = req.POST.get("pay_by")
        student = Student.objects.get(id=student_id)
        abonnement = Abonnement.objects.get(id=abonnement_id)
        # # SHEQUE FILE 
        # cheque_file = req.FILES['cheque_file']
        # fs = FileSystemStorage()
        # cheque_file = fs.save(cheque_file.name, cheque_file)
        # uploaded_file_url = fs.url(cheque_file)
        # CREATE PAYMENT if SHEQUE
        payment = Payment (student = student,abonnement=abonnement,payment_method=pay_method,created_by=pay_by)
       
        if payment:
            payment.save()
            student = payment.student
            price = abonnement.price
            context={
                "student":student,
                "price":price,
                "payment":payment,
            }
            return render(req,"payment/total.html",context)
    context = {
        "students":students,
        "abonnements":abonnements,
    }
    return render(req,"payment/test.html",context)


def Total(req,id):
    pay = Payment.objects.get(id=id)
    if req.method =="POST":
        total = req.POST.get("total")
        payed = req.POST.get("gived")
        rest = req.POST.get("rest")
        context = {
            "rest": rest
        }
    return render(req,"payment/total-detail.html", context)
    




def Detail(req,id):
    payment = Payment.objects.get(id=id)
    context ={
        'payment': payment
    }
    return render(req, "payment/detail.html", context)


def Pdf(req):
   
    return render(req, "payment/pdf.html")


def payment_pdf_view(request,*args,**kwargs):
    pk = kwargs.get('pk')
    payment = get_object_or_404(Payment, pk=pk)

    template_path = 'payment/detail.html'
    context = {'payment': payment}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class PaymentPdfView(PdfMixin, DetailView): #/** FOR EVERY Payment  **/
    model = Payment
    template_name = "payment/pdf.html"
    def get_context_data(self, **kwargs):
        
        context = super(PaymentPdfView, self).get_context_data(**kwargs)
        payment = Payment.objects.get(pk=self.kwargs.get('pk'))
        context ={
            "payment":payment

        }
        return context