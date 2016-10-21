from django import forms
from core.models import Project
from tinymce.widgets import TinyMCE

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        widgets = {
          'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }
        fields = '__all__'