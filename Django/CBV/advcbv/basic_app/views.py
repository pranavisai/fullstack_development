from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .import models

#This was the basic way to get a httpresponse from a classbased view.
#class CBView(View):
    #def get(self, request):
        #return HttpResponse("CLASS BASED VIEWS")

class IndexView(TemplateView):
    template_name = 'index.html'

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['injected'] = 'BASIC INJECTION!'
        #return context

class SchoolListView(ListView): #which will list out all the schools in the listview
    context_object_name = 'schools' #this way we can maintain the name instead of the software automatically adding _list at the end of the name
    model = models.School

class SchoolDetailView(DetailView): #will show all the details of a specific entry
    context_object_name = 'school_detail' #the name detailview sends out is just the classname in lowercase in this case 'school'
    model = models.School
    template_name = 'basic_app/school_detail.html'

#all these classes below are for the CRUD operations 
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")