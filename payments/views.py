from multiprocessing import context
from django.shortcuts import redirect, render
from core.models import Abonnement, Payment, Student
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

def Edit(req,id):
    payment = Payment.objects.get(id=id)
    form = PaymentForm(instance=payment)
    if req.method =="POST":
        form = PaymentForm(req.POST,instance=payment)
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
    
    if req.method =="POST":
        student_id = req.POST.get("student")
        abonnement_id = req.POST.get("abonnement")
        pay_method = req.POST.get("pay_method")
        pay_by = req.POST.get("pay_by")
        student = Student.objects.get(id=student_id)
        student = Student.objects.get(id=student_id)
        abonnement = Abonnement.objects.get(id=abonnement_id)
        # CREATE PAYMENT
        payment = Payment (student = student,abonnement=abonnement,payment_method=pay_method,created_by=pay_by)
        if payment:
            payment.save()
            student = payment.student
            price = abonnement.price
            context={
                "student":student,
                "price":price,

            }
            return render(req,"payment/total.html",context)
    context = {
        "students":students,
        "abonnements":abonnements,
    }
    return render(req,"payment/test.html",context)

