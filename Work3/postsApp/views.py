from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Post


class CustomLoginView(LoginView):
   template_name = 'postsApp/login.html'
   fields = '__all__'
   redirect_authenticated_user = True

   def get_success_url(self):
      return reverse_lazy('posts')

class RegistrationPage(FormView):
   template_name = 'postsApp/registration.html'
   form_class = UserCreationForm
   redirect_authenticated_user = True
   success_url = reverse_lazy('posts')

   def form_valid(self, form):
      user = form.save()
      if user is not None:
         login(self.request, user)
      return super(RegistrationPage, self).form_valid(form)

   def get(self, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('posts')
      return super(RegistrationPage, self).get(*args, **kwargs)


class PostsList(LoginRequiredMixin, ListView):
   model = Post
   context_object_name = 'postlist'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['postlist'] = context['postlist'].filter(user=self.request.user)
      return context


class PostsDetail(LoginRequiredMixin, DetailView):
   model = Post
   context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
   model = Post
   fields = ['title', 'description']
   success_url = reverse_lazy('posts')

   def form_valid(self, form):
      form.instance.user = self.request.user
      return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
   model = Post
   fields = ['title', 'description']
   success_url = reverse_lazy('posts')


class PostDelete(LoginRequiredMixin, DeleteView):
   model = Post
   context_object_name = 'post'
   success_url = reverse_lazy('posts')

