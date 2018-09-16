from django import forms
from .models import ProjectDef, WorkLog

class ProjectDefForm(forms.ModelForm):
    class Meta:
        model=ProjectDef
        fields='__all__'

class WorkLogForm(forms.ModelForm):
    #start= forms.DateField(
                # widget=forms.TextInput(attrs={'class':'datePicker'}))
    #end=start= forms.DateField(
                # widget=forms.TextInput(attrs={'class':'datePicker'}))
    class Meta:
        model=WorkLog
        fields='__all__'