from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Project, MyResumeModel


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class WebContentForm(ModelForm):
    class Meta:
        model = MyResumeModel
        fields = '__all__'
