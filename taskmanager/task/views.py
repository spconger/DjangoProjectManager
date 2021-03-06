from django.shortcuts import render, get_object_or_404
from .models import ProjectDef, WorkLog
from .forms import ProjectDefForm, WorkLogForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    project_list=ProjectDef.objects.all()
    return render(request, 'task/index.html', {'project_list': project_list} )

def detail(request, id):
    proj=get_object_or_404(ProjectDef, pk=id)
    return render(request, 'task/detail.html',{'proj': proj})

def logs(request):
    log_list=WorkLog.objects.all()
    return render(request, 'task/logs.html', {'log_list': log_list})

#class ProjectCreate(CreateView):
   # model=ProjectDef
    #fields='__all__'
@login_required
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
    
@login_required
def worktimes(request):
    form=WorkLogForm()
    if request.method=='POST':
        form=WorkLogForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            
        else:
            form=WorkLogForm()
    return render(request, 'task/worktimes.html', {'form': form})
   
def logoutmessage(request):
    return render(request, 'task/logoutmessage.html')

def loginmessage(request):
    return render(request, 'task/loginmessage.html')