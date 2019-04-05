from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile,Project,Votes
from .forms import ProfileForm,ProjectForm,VotesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
# Create your views here.
def welcome(request):
    projects=Project.objects.all() 
    return render(request, 'index.html',{"projects":projects})
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
@login_required(login_url='/accounts/login/')
def more(request, id):
        project= Project.objects.get(id=id)
        votes = Votes.objects.filter(project=project.id).all()

        design=0
        usability=0
        content=0
        number = len(votes)
        for r in votes:
                design+=round(r.design/number)
                usability+=round(r.usability/number)
                content+=round(r.content/number)

        return render(request,'more.html',{"project":project,"votes":votes,"usability":usability,"design":design,"content":content})
def vote(request, id):
        current_user = request.user
        post = Project.objects.get(id=id)
        votes = Votes.objects.filter(project=post)
        # print(comments)
        form = VotesForm()
        if request.method == 'POST':
                vote = VotesForm(request.POST,request.FILES)
                if vote.is_valid():
                        design = vote.cleaned_data['design']
                        usability= vote.cleaned_data['usability']
                        content = vote.cleaned_data['content']
                        rate = Votes(design = design,usability =usability,content=content,user=request.user,project=post)
                        rate.save()
                        return redirect("home")
                    
                
        else:
                return render(request, 'rate.html', {"form":form,'project':post,'user':current_user,'votes':votes})
@login_required(login_url='/accounts/login/')
def search(request):
    
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        project_found = Project.search_project(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'project_found':project_found})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
   

class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        all_merch = Project.objects.all()
        serializers = ProjectSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
