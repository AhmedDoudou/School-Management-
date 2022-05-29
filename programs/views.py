from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from core.models import Program
from django.views import generic
from django.urls import reverse_lazy


class ProgramCreateView(LoginRequiredMixin,CreateView):
    template_name = "program/create.html/"
    model = Program
    fields = ("__all__")
    success_url = reverse_lazy('program:list')
    def get_context_data(self, **kwargs):
        context = super(ProgramCreateView,self).get_context_data(**kwargs)
        page_title = 'Add program'
        context.update({
            "page_title":page_title
         })
        return context
    

class ProgramListView(LoginRequiredMixin, ListView):
    template_name = "program/list.html"
    context_object_name = "program/list"
    model = Program
    def get_context_data(self, **kwargs):
        context = super(ProgramListView,self).get_context_data(**kwargs)
        page_title = 'Program List'
        context.update({
            "page_title":page_title
         })
        return context


class ProgramUpdateView(LoginRequiredMixin, UpdateView):
    model = Program
    template_name = "program/update.html"
    fields = '__all__'
    success_url =reverse_lazy('program:list')
    def get_context_data(self, **kwargs):
        context = super(ProgramUpdateView,self).get_context_data(**kwargs)
        page_title = 'Update program'
        context.update({
            "page_title":page_title
         })
        return context


class ProgramDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "program/detail.html"
    context_object_name = "program Detail "
    model = Program
    success_url =reverse_lazy('program:list')


class ProgramDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "program/delete.html"
    model = Program
    success_url = reverse_lazy('program:list')
