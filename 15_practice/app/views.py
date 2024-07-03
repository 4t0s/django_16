from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView

class PostView(ListView):
    paginate_by = 2
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'recipes'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'recipe'
    pk_url_kwarg = 'id'
    
class CreatePost(CreateView, FormView):
    template_name = 'post_form.html'
    model = Post
    success_url = reverse_lazy('list')
    form_class = PostForm
    
    