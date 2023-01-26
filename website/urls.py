from django.urls import path
from .import views 
urlpatterns = [
    path('',views.home, name='home' ),
    path('about/',views.about, name='about' ),
    path('departments/',views.departments, name='departments' ),
    path('department/',views.department, name='department' ),
    path('calendar/',views.calendar, name='calendar' ),
    path('blog/',views.blog, name='blog' ),
    path('contact/',views.contact, name='contact' ),
]