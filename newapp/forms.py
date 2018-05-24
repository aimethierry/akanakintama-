from django import forms 
from .models import Post, Image
from app.models import Comment

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image',]


class PostForm(forms.ModelForm):
    
    
    class Meta:
        model = Post
        fields = ['title', 'description', 'text', ]


class CommentForm(forms.ModelForm):

    
    name = forms.CharField(required=True ,label="", widget=forms.TextInput(
        attrs={'placeholder':"enter your name", "class":"form-control"}
    ))

    text = forms.CharField(required=True, label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Leave a comment", 
                            "class": "form-control"}
                    ))


    class Meta:
        model = Comment
        fields = ['name', 'text', ]