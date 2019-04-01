from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile,Project,Votes
from .forms import ProfileForm,ProjectForm,VotesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
# Create your views here.
def welcome(request):
    return render(request, 'index.html')
@login_required(login_url='/accounts/login/')
def prof(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user=user)
    
    return render(request, 'all-awards/profile.html',{"profiles":profiles},{"user":user})
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user =request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
             profile = form.save(commit=False)
             profile.user = current_user
             profile.save()
        return redirect("home")
       
    else:
            form = ProfileForm()
    return render(request, 'new_profile.html',{"form":form})
@login_required(login_url='/accounts/login/')
def project(request):
    current_user = request.user
    if request.method =='POST':
        form =  ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect("home")    
    else:  
            form = ProjectForm()
    return render(request,'new-project.html',{"form":form})