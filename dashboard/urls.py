from django.urls import path
from .import views 
urlpatterns = [
    path('',views.dashboard, name='dashboard' ),
    path('details/',views.school_info, name='info' ),
    
    path('show-departments/',views.show_departments, name='departments' ),
    path('add-department/',views.add_department, name='add-department' ),
    path('edit-department/<int:pk>/', views.edit_department, name='edit-department'),
    path('delete-department/<int:pk>/', views.delete_department, name='delete-department'),

    path('teams/',views.show_team_members, name='teams' ),
    path('add-team/',views.add_team_member, name='add-team' ),

    path('staff/',views.show_staff, name='staff' ),
    path('add-staff/',views.add_staff, name='add-staff'),

     path('blogs/',views.show_blogs, name='blogs' ),
    path('add-blog/',views.add_blog, name='add-blog'),

     path('events/',views.show_events, name='events' ),
    path('add-event/',views.add_blog, name='add-event'),

 
 
]