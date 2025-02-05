from django import forms
from .models import KnowledgeTree
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class KnowledgeTreeForm(forms.ModelForm):
    class Meta:
        model = KnowledgeTree
        fields = ['title', 'data']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '请输入知识点树名称'
            }),
            'data': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 20,
                'placeholder': '请输入 JSON 格式的知识点树数据'
            })
        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")