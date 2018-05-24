from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.generic import View

from .forms import ImageForm, PostForm
from app.forms import BlogForm, ContactForm
from .models import Image
from app.models import Blog, Comment
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.template import RequestContext
from django.forms import modelformset_factory
from .forms import CommentForm


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





class BasicUploadView(FormView):
    form_class = ImageForm
    template_name = 'photo/basic_upload/index.html'  # Replace with your template.
    success_url = './'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                form.save()
            return self.form_valid(form)
        else:
            return HttpResponse("form is invalid")



def form(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)
    if request.method == 'POST':
        form = PostForm(request.POST)

        formset = ImageFormSet(request.POST, request.FILES,
                           queryset=Image.objects.none())
       

        if form.is_valid() and  formset.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Image(post=form, image=image)
                photo.save()
               
            
            return HttpResponse("saved")
        else:
            return HttpResponse("got error")
    else:
        form = PostForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'photo/basic_upload/index.html',
                  {'postForm': form, 'formset': formset},
                  context_instance=RequestContext(request))





def upload(request):
    return render()





def post(request):

    ImageFormSet = modelformset_factory(Image,
                                        form=ImageForm, extra=3)

    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Image.objects.none())


        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post_form, image=image)
                photo.save()
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print postForm.errors, formset.errors
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'index.html',
                  {'postForm': postForm, 'formset': formset},
                  context_instance=RequestContext(request))




def dashboard(request):
    return render(request, "dashboard.html")



def add_coment(request, pk):
   post= get_object_or_404(Blog, pk=pk)
   if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
          comment = form.save(commit=False)
          comment.post= post
          comment.save()
          return redirect('post_detail', slug=post.slug)
   else:
       form = CommentForm()
   return render(request, 'detail.html', {'form':form})