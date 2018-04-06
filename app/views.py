from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Blog
from django.views.generic.edit import CreateView
from .forms import BlogForm


class HomeView(TemplateView):
    template_name = "home.html"


class BlogView(ListView):
    model = Blog
    paginate_by = 4
    template_name = "blog.html"


class ContactView(TemplateView):
    template_name="contact.html"\


class AboutView(TemplateView):
    template_name="about.html"


def dashboard(request):
    return render(request, "dashboard.html")


class BlogCreate(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = '/blog/create/'