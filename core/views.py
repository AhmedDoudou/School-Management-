import datetime
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView  
from .models import *
from django.views import generic
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

 
class Login(LoginView):
    template_name = "registration/login.html"
    def get_context_data(self, **kwargs):
        context = super(Login,self).get_context_data(**kwargs)
        page_title = 'Login'
        context.update({
            "page_title":page_title
         })
        return context
        

class DashbordView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard.html"
    def get_context_data(self, **kwargs):
        context = super(DashbordView, self).get_context_data(**kwargs)
        page_title = 'Dashboard'
        # counting Total of students
        total_students = Student.objects.all().count()
         # students in 30 days ago
        thirty_days = datetime.date.today() - datetime.timedelta(days=30)
        last_thirty_days = Student.objects.filter(date_added__gte=thirty_days).count()
        sub_students = Inscription.objects.all().count()
        # All models
        student = Student.objects.all()
        program = Program.objects.all()
        contact = Parent.objects.all()
        inscription = Inscription.objects.all()
        context.update({
            "total_students": total_students,
            "last_thirty_days": last_thirty_days,
            "sub_students": sub_students,
            "student": student,
            "program": program,
            "inscription":inscription,
            "contact":contact,
            "page_title":page_title
         })
        return context