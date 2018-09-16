from django.shortcuts import render, get_object_or_404
from .models import ProjectDef
from .forms import ProjectDefForm, WorkLogForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    project_list=ProjectDef.objects.all()
    return render(request, 'task/index.html', {'project_list': project_list} )

def detail(request, id):
    proj=get_object_or_404(ProjectDef, pk=id)
    return render(request, 'task/detail.html',{'proj': proj})

#class ProjectCreate(CreateView):
   # model=ProjectDef
    #fields='__all__'

def newproject(request):
    form=ProjectDefForm()
    
    if request.method=='POST':
        form=ProjectDefForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
        else:
            form=ProjectDefForm()
    return render(request, 'task/newproject.html', {'form': form})

def worktimes(request):
    form=WorkLogForm()
    if request.method=='POST':
        form=ProjectDefForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            
        else:
            form=WorkLogForm()
    return render(request, 'task/worktimes.html', {'form': form})