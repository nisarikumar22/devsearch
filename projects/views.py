from django.shortcuts import render, redirect
from .models import Project, Reviews, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.



# sending a http responce
def projects(request):
    all_projects = Project.objects.all()
    context = {'projects':all_projects}
    
    return render(request, 'projects/projects.html',context)

def project(request, pk):
    project_obj = Project.objects.get(id = pk)
    tags = project_obj.tags.all()
    context = {
        'p_obj': project_obj,
    }
    return render(request, 'projects/single-project.html',context)

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    project_obj = Project.objects.get(id = pk)
    form = ProjectForm(instance=project_obj)

    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES, instance=project_obj)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    project_obj = Project.objects.get(id = pk)

    if request.method == "POST":
        project_obj.delete()
        return redirect('projects')
    
    context = {'object': project_obj}

    return render(request, 'projects/delete-confirm.html', context)
