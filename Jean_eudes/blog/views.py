from msilib.schema import Class, ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView,DetailView
# Create your views here.
class PostListView(ListView):
    model = Post 
class PostCreateView(CreateView):
    model = Post
    fields= '__all__'
    success_url = reverse_lazy('blog:all')
class PostDetailView(DetailView):
    model = Post
