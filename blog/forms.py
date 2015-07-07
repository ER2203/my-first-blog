'''
Created on 7 jul. 2015

@author: ed
'''
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
