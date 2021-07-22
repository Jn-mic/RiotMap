from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import fields
from .models import *
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.Form):
    class Meta:
        model=Post
        fields=['name','description','image']

class ProfileForm(forms.ModelForm):
    class Meta:
        fields=['profile_image']

class HotspotForm(forms.ModelForm):
    class Meta:
        model=Hotspot
        fields=['name','city','location']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfleUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['profile_image', 'bio']

class WorkForm(forms.ModelForm):

    class Meta:
        model=Work
        fields=['name','address','city']

class HospitalForm(forms.ModelForm):

    class Meta:
        model=Hospital
        fields=['name','address','city']

class PoliceForm(forms.ModelForm):

    class Meta:
        model=Police
        fields=['name','address','city']





