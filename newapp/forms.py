from django import forms 
from .models import Post, Image

class PostForms(forms.ModelForm):

    class Meta:
        models = Post
        fields = ['title', 'description', 'text']


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image') 

    class Meta:
        model = Image
        fields = ['image',]