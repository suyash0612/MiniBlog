from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import PostModel
from django.contrib.auth.models import Group

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def homePage(request):
    posts = PostModel.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def aboutPage(request):
    return render(request,'blog/about.html')

def contactPage(request):
    return render(request,'blog/contact.html')

def dashboardPage(request):
    if request.user.is_authenticated:
        posts = PostModel.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,"full_name":full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

def signupPage(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations User, Your Author account has been created')
            user = form.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)

    else:
        form = SignupForm()

    return render(request,'blog/signup.html',{'form':form})

def loginPage(request):
    # print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,' Logged in successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/')

def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = PostModel(title = title, desc = desc)
                post.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formdata = PostModel.objects.get(pk=id)
            form = PostForm(request.POST,instance=formdata)
            if form.is_valid():
                form.save()
                form = PostForm()
        else:
            formdata = PostModel.objects.get(pk=id)
            form = PostForm(instance=formdata)
            if request.GET.get('clearform') == 'clearform':
                form = PostForm()
        return render(request, 'blog/updatepost.html',{'form':form,'id':id})
    else:
        return HttpResponseRedirect('/login/')
    
def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formdata = PostModel.objects.get(pk=id)
            formdata.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
    

        