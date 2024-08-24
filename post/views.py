from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.views.generic.edit import CreateView,DeleteView
from .models import Post
# Create your views here.

class HomePageView(ListView):

    model= Post
    template_name= "home.html"


class DetailPageView(DetailView):

    model=Post
    template_name= "detail.html"

class CreatePageView(CreateView):

    model=Post
    template_name="create.html"

    fields=["titulo","descripcion","autor"]
    success_url=reverse_lazy("home")

class DeletePageView(DeleteView):

    model=Post
    template_name="delete.html"
    success_url=reverse_lazy("home")