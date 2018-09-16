from django import forms
from .models import ProjectDef, WorkLog

class ProjectDefForm(forms.ModelForm):
    class Meta:
        model=ProjectDef
        fields='__all__'

class WorkLogForm(forms.ModelForm):
    class Meta:
        model=WorkLog
        fields='__all__'