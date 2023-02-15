from django.shortcuts import render,redirect
from website.models import Department, Team_Member, Staff, Blog, Event,School_Information
from dashboard.models import SMS
from .forms import DepartmentForm,TeamForm, StaffForm, BlogForm, EventForm
# User authentication start 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests




# 
# ============USER AUTHENTICATION , LOGIN AND LOGOUT==========
# ============================================================
def loginUser(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'User succesfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid username or password')
    context ={}
    return render(request,'dashboard/login.html', context)   


def logoutUser(request):
    logout(request)
    return redirect('login')


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

    
    

    context = {'department_count':department_count,'team_member_count':team_member_count,'staff_count':staff_count,'post_count':post_count, 'event_count':event_count, 'departments':departments, 'team_member':team_member, 'staff':staff,'events':events,'blogs':blogs, }
    return render(request, 'dashboard/dashboard.html',context)


def school_info(request):
    info = School_Information.objects.first()

    context = {'info':info}
    return render(request, 'dashboard/school_information.html',context)


# ================DEPARTMENT BEGINS =========
# ================DEPARTMENT BEGINS =========
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

# @login_required(login_url='login')
def edit_department(request,pk):
    department = Department.objects.get(pk=pk)
    form = DepartmentForm(instance=department)
    

    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES,instance=department)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'forms': form, 'department':department}
    return render(request, 'dashboard/add_department.html', context)


# @login_required(login_url='login')
def delete_department(request,pk):
    department = Department.objects.get(pk=pk)

    if request.method == 'POST':
        department.delete()
        return redirect('departments')
    return redirect('departments')

# ================DEPARTMENT ENDS =========
# ================DEPARTMENT ENDS =========

def show_team_members(request):
    teams = Team_Member.objects.all()
    
    context = {'teams':teams}
    return render(request, 'dashboard/show_team_members.html', context)

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
    return render(request, 'dashboard/add_team_member.html', context)


# @login_required(login_url='login')
def edit_team(request,pk):
    team = Team_Member.objects.get(pk=pk)
    form = TeamForm(instance=team)
    

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES,instance=team)
        if form.is_valid():
            form.save()
            return redirect('teams')
    context = {'forms': form}
    return render(request, 'dashboard/add_team_member.html', context)


# @login_required(login_url='login')
def delete_team(request,pk):
    team = Team_Member.objects.get(pk=pk)

    if request.method == 'POST':
        team.delete()
        return redirect('teams')
    return redirect('teams')

# ================DEPARTMENT ENDS =========
# ================DEPARTMENT ENDS =========



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


# @login_required(login_url='login')
def edit_staff(request,pk):
    staff = Staff.objects.get(pk=pk)
    form = StaffForm(instance=staff)
    

    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES,instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff')
    context = {'forms': form}
    return render(request, 'dashboard/add_staff.html', context)


# @login_required(login_url='login')
def delete_staff(request,pk):
    staff = Staff.objects.get(pk=pk)

    if request.method == 'POST':
        staff.delete()
        return redirect('staff')
    return redirect('staff')

# ================DEPARTMENT ENDS =========
# ================DEPARTMENT ENDS =========

def show_blogs(request):
    blogs = Blog.objects.all()

    context = {'blogs':blogs}
    return render(request, 'dashboard/show_blogs.html', context)

def add_blog(request):
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs')           
        else:
            messages.error(request, form.errors)
    else:
        form = BlogForm()
    context = {'forms': form}
    return render(request, 'dashboard/add_blog.html', context)



# @login_required(login_url='login')
def edit_blog(request,pk):
    blog = Blog.objects.get(pk=pk)
    form = BlogForm(instance=blog)
    

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    context = {'forms': form}
    return render(request, 'dashboard/add_blog.html', context)


# @login_required(login_url='login')
def delete_blog(request,pk):
    staff = Staff.objects.get(pk=pk)

    if request.method == 'POST':
        staff.delete()
        return redirect('blogs')
    return redirect('blogs')

# ================DEPARTMENT ENDS =========
# ================DEPARTMENT ENDS =========
def show_events(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'dashboard/show_events.html', context)

def add_events(request):
    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events')
            
        else:
            messages.error(request, form.errors)

    else:
        form = EventForm()
    context = {'forms': form}
    return render(request, 'dashboard/add_event.html', context)


# @login_required(login_url='login')
def edit_event(request,pk):
    event = Event.objects.get(pk=pk)
    form = EventForm(instance=event)
    

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES,instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')
    context = {'forms': form}
    return render(request, 'dashboard/add_event.html', context)


# @login_required(login_url='login')
def delete_event(request,pk):
    staff = Event.objects.get(pk=pk)

    if request.method == 'POST':
        staff.delete()
        return redirect('events')
    return redirect('events')

# ================DEPARTMENT ENDS =========
# ================DEPARTMENT ENDS =========
def show_sms(request):

    sms = SMS.objects.all()    
    context = {'sms': sms}
    return render(request, 'dashboard/show_sms.html',context)



def send_sms(request):
    if request.method == 'POST':
        staff = Staff.objects.all()
        
        sender_id = request.POST.get('sender_id')
        title = request.POST.get('title')
        body = request.POST.get('body')
        message_count = len(staff)
        message = ", ".join([title, body]) 
        print(message)

        # print(len(parents))
        for worker in staff:
            to_number =str(worker.contact)
            # print(parent.phone)
            
            API_KEY = "OjRHbjdNV0doSXRUOFRTb0s="
            if to_number and len(to_number)==10 and to_number.startswith("0"):

                url = f"https://sms.arkesel.com/sms/api?action=send-sms&api_key={API_KEY}&to={to_number}&from={sender_id}&sms={message}"
                print(url)
                res = requests.get(url)
                print(worker.contact)
                print(res.status_code)
                print(res.content)
        
               
            else:
                print("invalid phone number")
        SMS.objects.create(
                sender_id=sender_id,
                title=title,
                body=body,
                messages_sent=message_count
               )
        return redirect('sms')
    context = {}
    return render(request, 'dashboard/send_sms.html',context)


    # HOW TO FILL SHOW TABLE WITH INFO FROM SEND_SMS





