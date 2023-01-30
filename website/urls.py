from django.urls import path
from .import views 
urlpatterns = [
    path('',views.home, name='home' ),
    path('about/',views.about, name='about' ),
    path('departments/',views.departments, name='departments' ),
    path('departments/<int:pk>/',views.department, name='department' ),
    path('calendar/',views.calendar, name='calendar' ),
    path('blogs/',views.blogs, name='blogs' ),
    path('blogs/<int:pk>/',views.blog, name='blog' ),
    path('contact/',views.contact, name='contact' ),
]