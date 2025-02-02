from django import forms
from .models import KnowledgeTree

class KnowledgeTreeForm(forms.ModelForm):
    class Meta:
        model = KnowledgeTree
        fields = ['data']
        widgets = {
            'data': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 20,
                'placeholder': '请以 JSON 格式录入知识树结构，例如：{"学科": {"课本名": {"章节": ["知识点1", "知识点2"]}}}'
            }),
        }
