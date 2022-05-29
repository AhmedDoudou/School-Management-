from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from core.models import Parent
from django.views import generic
from django.urls import reverse_lazy


class ParentCreateView(LoginRequiredMixin,CreateView):
    template_name = "parent/create.html/"
    model = Parent
    fields = ("__all__")
    success_url = reverse_lazy('parent:list')
    def get_context_data(self, **kwargs):
        context = super(ParentCreateView,self).get_context_data(**kwargs)
        page_title = 'Add parent'
        context.update({
            "page_title":page_title
         })
        return context
    

class ParentListView(LoginRequiredMixin, ListView):
    template_name = "parent/list.html"
    context_object_name = "parent/list"
    model = Parent
    def get_context_data(self, **kwargs):
        context = super(ParentListView,self).get_context_data(**kwargs)
        page_title = 'Parent List'
        context.update({
            "page_title":page_title
         })
        return context


class ParentUpdateView(LoginRequiredMixin, UpdateView):
    model = Parent
    template_name = "parent/update.html"
    fields = '__all__'
    success_url =reverse_lazy('parent:list')
    def get_context_data(self, **kwargs):
        context = super(ParentUpdateView,self).get_context_data(**kwargs)
        page_title = 'Update parent'
        context.update({
            "page_title":page_title
         })
        return context


class ParentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "parent/detail.html"
    context_object_name = "parent Detail "
    model = Parent
    success_url =reverse_lazy('parent:list')


class ParentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "parent/delete.html"
    model = Parent
    success_url = reverse_lazy('parent:list')
