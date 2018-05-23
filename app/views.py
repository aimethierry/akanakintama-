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
from newapp.forms import ImageForm, PostForms

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



# def post(request):

#     ImageFormSet = modelformset_factory(Image,
#                                         form=ImageForm, extra=3)

#     if request.method == 'POST':

#         postForm = PostForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES,
#                                queryset=Images.objects.none())


#         if postForm.is_valid() and formset.is_valid():
#             post_form = postForm.save(commit=False)
#             post_form.user = request.user
#             post_form.save()

#             for form in formset.cleaned_data:
#                 image = form['image']
#                 photo = Images(post=post_form, image=image)
#                 photo.save()
#             messages.success(request,
#                              "Yeeew, check it out on the home page!")
#             return HttpResponseRedirect("/")
#         else:
#             (print postForm.errors, formset.errors)
#     else:
#         postForm = PostForm()
#         formset = ImageFormSet(queryset=Images.objects.none())
#     return render(request, 'try.html',
#                   {'postForm': postForm, 'formset': formset},
#                   context_instance=RequestContext(request))