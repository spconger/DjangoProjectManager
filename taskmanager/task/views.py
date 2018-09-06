from django.shortcuts import render, get_object_or_404
from .models import ProjectDef

# Create your views here.
def index(request):
    project_list=ProjectDef.objects.all()
    return render(request, 'task/index.html', {'project_list': project_list} )

def detail(request, id):
    proj=get_object_or_404(ProjectDef, pk=id)
    return render(request, 'task/detail.html',{'proj': proj})
