from django import forms
from .models import Project, Profile, Votes 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class VotesForm(forms.ModelForm):
    class Meta:
        model = Votes
        exclude = ['user','project','posted_on']

