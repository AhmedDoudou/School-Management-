from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from core.models import *
from django.contrib import messages
from studentManagement.forms import StudentForm
from parents.forms import ParentForm
from .forms import InscriptionForm



from django.views import generic
from django.urls import reverse_lazy


class InscriptionCreateView(LoginRequiredMixin,CreateView):
    template_name = "inscription/create.html/"
    model = Inscription
    fields = ("__all__")
    success_url = reverse_lazy('inscription:list')
    def get_context_data(self, **kwargs):
        context = super(InscriptionCreateView,self).get_context_data(**kwargs)
        page_title = 'Add inscription'
        context.update({
            "page_title":page_title
         })
        return context


def NewInsc(request):
    template_name = "inscription/new.html/"
    students = Student.objects.all()
    parents  = Parent.objects.all()
    programs = Program.objects.all()
    memberships = Membership.objects.all()
    student_form = StudentForm
    parent_form = ParentForm
    last_student = Student.objects.last()
    last_parent = Parent.objects.last()
    
    # def new_student(req):
    #     if req.method == 'POST':
    #         student_form = StudentForm(req.POST)
    #         if student_form.is_valid() :
    #             student_form.save()
    # def new_parent(req):
    #     if request.method == "POST":
    #         student_form = StudentForm(request.POST)
    #         if parent_form.is_valid():
    #             parent_form.save()
    if request.method == "POST":
            student_id     = request.POST.get("student_id")
            parent_id      = request.POST.get('parent_id')
            program_id     = request.POST.get('program_id')
            membership_id  = request.POST.get('membership_id')
            student        = Student.objects.get(id=student_id)
            parent         = Parent.objects.get(id=parent_id)
            program        = Program.objects.get(id=program_id)
            membership     = Membership.objects.get(id=membership_id)
            inscription    = Inscription(student=student,parent=parent,program=program,membership=membership)
            inscription.save()
            
    context = {
        'student_form': student_form,
        'parent_form': parent_form,
        'students'   : students,
        'parents'   : parents,
        'programs'   : programs,
        'memberships' : memberships,
        'last_student': last_student,
        'last_parent': last_parent,

    }
    return render(request, template_name,context) 

class InscriptionListView(LoginRequiredMixin, ListView):
    template_name = "inscription/list.html"
    context_object_name = "inscription/list"
    model = Inscription
    def get_context_data(self, **kwargs):
        context = super(InscriptionListView,self).get_context_data(**kwargs)
        page_title = 'inscription List'
        context.update({
            "page_title":page_title
         })
        return context


class InscriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = Inscription
    template_name = "inscription/update.html"
    fields = '__all__'
    success_url =reverse_lazy('inscription:list')
    def get_context_data(self, **kwargs):
        context = super(InscriptionUpdateView,self).get_context_data(**kwargs)
        page_title = 'Update inscription'
        context.update({
            "page_title":page_title
         })
        return context


class InscriptionDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "inscription/detail.html"
    context_object_name = "inscription Detail "
    model = Inscription
    success_url =reverse_lazy('inscription:list')


class InscriptionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "inscription/delete.html"
    model = Inscription
    success_url = reverse_lazy('inscription:list')
