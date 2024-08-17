from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import CreateView
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
