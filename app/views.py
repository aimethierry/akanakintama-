from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Blog
from django.views.generic.edit import CreateView
from .forms import BlogForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.views.generic.detail import DetailView

class HomeView(TemplateView):
    template_name = "home.html"


class BlogView(ListView):
    model = Blog
    paginate_by = 4
    template_name = "blog.html"


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Email = form.cleaned_data['Email']
            subject = form.cleaned_data['subject']
           
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, Email, ['akanakintamaange@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
    return render(request, "contact.html", {'form': form})




class AboutView(TemplateView):
    template_name="about.html"


def dashboard(request):
    return render(request, "dashboard.html")


class BlogCreate(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = '/blog/create/'


class BlogDetail(DetailView):
    model = Blog
    template_name = 'detail.html'
