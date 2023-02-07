from django.shortcuts import render,redirect
from website.models import Department, Team_Member, Staff, Blog, Event,School_Information
from .forms import DepartmentForm,TeamForm, StaffForm, BlogForm, EventForm
from django.contrib import messages


# DASHBOARD
def dashboard(request):
    departments = Department.objects.all()
    team_member = Team_Member.objects.all()
    events = Event.objects.all()
    staff = Staff.objects.all()
    blogs = Blog.objects.all()
    department_count = Department.objects.count()
    team_member_count = Team_Member.objects.count()
    staff_count = Staff.objects.count()
    post_count = Blog.objects.count()
    event_count = Event.objects.count()
    

    context = {'department_count':department_count,'team_member_count':team_member_count,'staff_count':staff_count,'post_count':post_count, 'event_count':event_count, 'departments':departments, 'team_member':team_member, 'staff':staff,'events':events,'blogs':blogs}
    return render(request, 'dashboard/dashboard.html',context)


def school_info(request):
    info = School_Information.objects.first()

    context = {'info':info}
    return render(request, 'dashboard/school_information.html',context)

def show_departments(request):
    departments = Department.objects.all()
    montessori_tutors = Staff.objects.filter(department='Montessori').count()
    lower_primary_tutors = Staff.objects.filter(department='Lower Primary').count()
    upper_primary_tutors = Staff.objects.filter(department='Upper Primary').count()
    jhs_tutors = Staff.objects.filter(department='JHS').count()

    context = {'departments':departments,'montessori_tutors':montessori_tutors,'lower_primary_tutors':lower_primary_tutors,'upper_primary_tutors':upper_primary_tutors,'jhs_tutors':jhs_tutors}
    return render(request, 'dashboard/show_department.html', context)


def add_department(request):
    form = DepartmentForm()

    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('departments')
            
        else:
            messages.error(request, form.errors)
            

    else:
        form = DepartmentForm()
    context = {'forms': form}
    return render(request, 'dashboard/add_department.html', context)

def show_team_member(request):
    team = Team_Member.objects.all()
    
    context = {'team':team}
    return render(request, 'dashboard/show_team_member.html', context)

def add_team_member(request):
    form = TeamForm()

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teams')
            
        else:
            messages.error(request, form.errors)
            

    else:
        form = TeamForm()
    context = {'forms': form}
    context = {}
    return render(request, 'dashboard/add_team_member.html', context)

def show_staff(request):
    staff = Staff.objects.all()

    context = {'staff':staff}
    return render(request, 'dashboard/show_staff.html', context)

def add_staff(request):
    form = StaffForm()

    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff')
            
        else:
            messages.error(request, form.errors)
            

    else:
        form = StaffForm()
    context = {'forms': form}
    return render(request, 'dashboard/add_staff.html', context)


def show_blogs(request):
    context = {}
    return render(request, 'dashboard/show_blogs.html', context)

def add_blog(request):
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff')
            
        else:
            messages.error(request, form.errors)
            

    else:
        form = BlogForm()
    context = {'forms': form}
    context = {}
    return render(request, 'dashboard/add_blog.html', context)


def show_events(request):
    context = {}
    return render(request, 'dashboard/show_events.html', context)

def add_events(request):
    context = {}
    return render(request, 'dashboard/add_event.html', context)

    



