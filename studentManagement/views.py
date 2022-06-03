from audioop import reverse
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView,TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from core.models import *
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.template.loader import get_template
from django_xhtml2pdf.utils import generate_pdf
from xhtml2pdf import pisa
# from django.views.generic.detail import DetailView
from django_xhtml2pdf.views import PdfMixin
from django_xhtml2pdf.utils import pdf_decorator
from django.core.files.storage import FileSystemStorage

from studentManagement.forms import StudentForm

class StudentCreateView(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    template_name = "student/create.html/"
    model = Student
    fields = ("__all__")
    success_url = reverse_lazy('student:list')
    success_message = "The Student Created successfully "
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView,self).get_context_data(**kwargs)
        page_title = 'Add Student'
        context.update({
            "page_title":page_title
         })
        return context
    

class StudentListView(LoginRequiredMixin, ListView):
    template_name = "student/list.html"
    context_object_name = "student/list"
    model = Student
    fields = ("__all__")
    def get_context_data(self, **kwargs):
        context = super(StudentListView,self).get_context_data(**kwargs)
        page_title = 'Student List'
        context.update({
            "page_title":page_title
         })
        return context


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = "student/update.html"
    fields = '__all__'
    success_url = reverse_lazy('student:list')
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView,self).get_context_data(**kwargs)
        page_title = 'Update Student'
        context.update({
            "page_title":page_title
         })
        return context


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "student/detail.html"
    context_object_name = "Student Detail "
    model = Student
    success_url ="/"

def Edit(req, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if req.method =="POST":
        form = StudentForm(req.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("student:list")
    context ={
        "form":form
    }
    return render(req,"student/edit.html",context)


def Detail(req,id):
    student = Student.objects.get(id=id)
    payment = Payment.objects.get(student=student)
    context ={
        "student":student,
        "payment":payment

    }
    return render(req,"student/detail.html",context)


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "student/delete.html"
    model = Student
    success_url = reverse_lazy('student:list')

def student_render_pdf_view(request,*args,**kwargs):
    pk = kwargs.get('pk')
    student = get_object_or_404(Student, pk=pk)

    template_path = 'student/detail.html'
    context = {'student': student}
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


class StudentPdfView(PdfMixin, DetailView):
    model = Student
    template_name = "student/pdf.html"

class StudentsPdfView(PdfMixin, ListView):
    model = Student
    template_name = "student/studentsPDF.html"
    model = Student
    fields = ("__all__")
    def get_context_data(self, **kwargs):
        context = super(StudentsPdfView,self).get_context_data(**kwargs)
        page_title = 'Students PDF'
        pdftoday = datetime.date.today()
        context.update({
            "page_title":page_title,
            "pdftoday": pdftoday
         })
        return context

class BlanckView(CreateView):
    template_name = "student/blanck.html/"
    model = Student
    fields = ("__all__")
    success_url = reverse_lazy('student:list')
    def get_context_data(self, **kwargs):
        context = super(BlanckView,self).get_context_data(**kwargs)
        page_title = 'Add Student'
        context.update({
            "page_title":page_title
         })
        return context


def NewInscription(req):
    template_name = "inscription/newinscription.html"
    memberships = Membership.objects.all()
    programs = Program.objects.all()
    context={
        'programs': programs,
        'memberships': memberships,
    }
    if req.method == 'POST':
        
        # ============= STUDENT ==============
        gender = req.POST.get("gender")
        first_name  = req.POST.get("first_name")
        last_name   = req.POST.get("last_name")
        phone       = req.POST.get("phone")
        grade       = req.POST.get("grade")
        birthday    = req.POST.get("birthday")
        print(birthday)
        status      = req.POST.get("status")
        email       = req.POST.get("email")
        gender      = req.POST.get("gender")
        address     = req.POST.get("address")
        if req.FILES['picture']:
            picture     = req.FILES['picture']
            fss         = FileSystemStorage()
            file        = fss.save(picture.name,picture)
            picture_url = fss.url(file)
        print(picture_url)
        # student.save()
        student  = Student(picture=picture_url,gender=gender,email=email,first_name=first_name,last_name=last_name,grade=grade,birthday=birthday,address=address,)
        student.save()
        last_student = Student.objects.last()
        # ============= PARENT ==============
        parent_gender   = req.POST.get("parent_gender")
        fullname        = req.POST.get("fullname")
        phone           = req.POST.get("phone")
        address         = req.POST.get("address")
        description     = req.POST.get("description")
        # parent.save()
        parent = Parent(parent_gender=parent_gender, fullname=fullname, phone=phone, address=address, description=description)
        parent.save()
        last_parent = Parent.objects.last()
        # ============= PROGRAM ==============
        program_id = req.POST.get('program_id')
        print(program_id)
        program = Program.objects.get(id=program_id)
        # ============= MEMBERSHIP ==============
        membership_id = req.POST.get('membership_id')
        print(membership_id)
        membership  = Membership.objects.get(id=membership_id)
        insc = Inscription(student =last_student,parent=last_parent,program=program, membership= membership )
        insc.save()

    return render(req, template_name, context)


class ChartView(TemplateView):
    template_name = "chart.html"
    def get_context_data(self, **kwargs):
        context = super(ChartView, self).get_context_data(**kwargs)
        Students = Student.objects.order_by_birthday()
        for student in Students:
            print(student)
        context.update({
            "qs": Students
        })
        print(context)
        return context

    

