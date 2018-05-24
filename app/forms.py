from django import forms
from .models import Blog
from newapp.models import Post, Image


class ContactForm(forms.Form):
    
    Email = forms.EmailField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"Email", "class":"form-control"}
    ))
    subject = forms.CharField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"subject", "class":"form-control"}
    ))

    message = forms.CharField(required=True, label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "describe your self", 
                            "class": "form-control"}
                    ))



class BlogForm(forms.ModelForm):

    title = forms.CharField(label='', 
                widget=forms.TextInput(
                        attrs={'placeholder': "Your title", 
                            "class": "form-control"}
                    ))

    text = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Leave your Text", 
                            "class": "form-control"}
                    ))
    class Meta:
        model = Blog
        fields = [
            'title',
            "text",
            "image",
            "image1",
            "image2",
            "image3",
        ]




