from django import forms
from projectapp.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title", "description", "url_image", "url_github", "tags")
        
