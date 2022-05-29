from multiprocessing import context
from django.shortcuts import redirect, render
from core.models import Payment
from .forms import PaymentForm

def List(req):
    payments = Payment.objects.all()
    context = {"payments":payments}
    return render(req, "payment/list.html",context)

def Add(req):
    form = PaymentForm
    if req.method =="POST":
        form = PaymentForm(req.POST)
        if form.is_valid():
            form.save()
            redirect("payment:list")
        else:
            form = PaymentForm()
    context = {"form":form}
    return render(req, "payment/add.html",context)