from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm, ProjectForm, WebContentForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .decorators import allowed_users


# Create your views here.
def home_page(request):
    web_content = MyResumeModel.objects.get(my_name='Rakesh Kumar')
    context = {'web_content': web_content}
    return render(request, 'rakesh/index.html', context)


def about_page(request):
    web_content = MyResumeModel.objects.get(my_name='Rakesh Kumar')
    context = {'web_content': web_content}
    return render(request, 'rakesh/about.html', context)


def resume_page(request):
    web_content = MyResumeModel.objects.get(my_name='Rakesh Kumar')
    context = {'web_content': web_content}
    return render(request, 'rakesh/resume.html', context)


def services_page(request):
    context = {}
    return render(request, 'rakesh/services.html', context)


def projects_page(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'rakesh/projects.html', context)


def contact_page(request):
    web_content = MyResumeModel.objects.get(my_name='Rakesh Kumar')
    context = {'web_content': web_content}
    return render(request, 'rakesh/contact.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'rakesh/login.html', context)


def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'rakesh/register.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


def proj_details_page(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'rakesh/project-details.html', context)


@allowed_users(allowed_user=['rakesh124'])
def dashboard(request):
    projects = Project.objects.all()
    web_content = MyResumeModel.objects.all()
    context = {'projects': projects,'web_content':web_content}
    return render(request, 'rakesh/dashboard.html', context)


@allowed_users(allowed_user=['rakesh124'])
def create_proj(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'rakesh/create_update_proj.html', context)


@allowed_users(allowed_user=['rakesh124'])
def update_proj(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            # print(request.POST.get())
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'rakesh/create_update_proj.html', context)


@allowed_users(allowed_user=['rakesh124'])
def delete_proj(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    context = {'project': project}
    return render(request, 'rakesh/delete_proj.html', context)


@allowed_users(allowed_user=['rakesh124'])
def update_web_content_form(request, pk):
    rakesh = MyResumeModel.objects.get(id=pk)
    form = WebContentForm(instance=rakesh)
    if request.method == 'POST':
        form = WebContentForm(request.POST, instance=rakesh)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'rakesh/update_web_form.html', context)
