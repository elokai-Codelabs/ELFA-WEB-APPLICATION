from django.shortcuts import render
from website.models import Department, Team_Member, Staff, Blog, Event,School_Information

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

    return render(request, 'dashboard/add_department.html')

