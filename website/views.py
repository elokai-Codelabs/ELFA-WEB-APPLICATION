from django.shortcuts import render
from .models import Department,School_Information, Team_Member,Event,Blog, Staff

# Create your views here.
def home(request):
    departments = Department.objects.all()
    info = School_Information.objects.first()
    teams = Team_Member.objects.all()

    context = {'departments':departments,'info':info,'teams':teams}
    return render(request, 'website/index.html',context)

def about(request):
    info = School_Information.objects.first()
    teams = Team_Member.objects.all()

    context = {'info':info,'teams':teams}
    return render(request, 'website/about.html',context)

def departments(request):
    
    departments = Department.objects.all()
  
    context = {'departments':departments}
    return render(request, 'website/departments.html',context)

def department(request,pk):
    
    department = Department.objects.get(id=pk)

    context = {'department':department}
    return render(request, 'website/department-inner.html',context)

def calendar(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'website/calendar.html',context)

def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'website/blog.html',context)

def blog(request,pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog':blog}
    return render(request, 'website/post.html',context)

def contact(request):
    info = School_Information.objects.first()

    context = {'info':info}
    return render(request, 'website/contact.html',context)

