from django.shortcuts import render
from website.models import Department, Team_Member, Staff, Blog, Event

# DASHBOARD
def dashboard(request):
    department = Department.objects.all()
    team_member = Team_Member.objects.all()
    event = Event.objects.all()
    department = Department.objects.all()
    department = Department.objects.all()
    department_count = Department.objects.count()
    team_member_count = Team_Member.objects.count()
    staff_count = Staff.objects.count()
    post_count = Blog.objects.count()
    event_count = Event.objects.count()
    

    context = {'department_count':department_count,'team_member_count':team_member_count,'staff_count':staff_count,'post_count':post_count, 'event_count':event_count}
    return render(request, 'dashboard/dashboard.html',context)