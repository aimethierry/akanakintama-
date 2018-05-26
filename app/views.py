from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Blog
from django.views.generic.edit import CreateView
from .forms import BlogForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from newapp.models import Image, Post
from newapp.forms import ImageForm, PostForm
from django.forms import modelform_factory
from django.http import JsonResponse
from newapp.forms import CommentForm
from django.views.generic import View


class HomeView(TemplateView):
    template_name = "home.html"


class BlogView(ListView):
    model = Blog
    paginate_by = 4
    template_name = "blog.html"


def contact(request):
    return HttpResponse("everything changed")





class AboutView(TemplateView):
    template_name="about.html"




class BlogCreate(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = '/blog/create/'


class BlogDetail(DetailView):
    model = Blog
    template_name = 'detail.html'
    form_class = CommentForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save
            return HttpResponse('/success/')
        return render(request, self.template_name, {'form': form})



class FormView(DetailView):
    form_class = CommentForm
    template_name = 'detail.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save
            return HttpResponse('/success/')

        return render(request, self.template_name, {'form': form})



class BlogList(ListView):
    model = Blog
    paginate_by = 4
    template_name = "dashboard-blog.html"


class BlogEdit(UpdateView):
    model = Blog
    template_name = "editblog.html"
    form_class = BlogForm


class BlogDelete(DeleteView):
    model = Blog
    success_url = '/dashboard/list/'
    template_name = "delete.html"




