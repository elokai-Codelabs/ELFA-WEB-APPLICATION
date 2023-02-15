from django.urls import path
from .import views 
urlpatterns = [

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('',views.dashboard, name='dashboard' ),
    path('details/',views.school_info, name='info' ),
    
    path('show-departments/',views.show_departments, name='departments' ),
    path('add-department/',views.add_department, name='add-department' ),
    path('edit-department/<int:pk>/', views.edit_department, name='edit-department'),
    path('delete-department/<int:pk>/', views.delete_department, name='delete-department'),

    path('teams/',views.show_team_members, name='teams' ),
    path('add-team/',views.add_team_member, name='add-team' ),
    path('edit-team/<int:pk>/',views.edit_team, name='edit-team' ),
    path('delete-team/<int:pk>/',views.delete_team, name='delete-team' ),

    path('staff/',views.show_staff, name='staff' ),
    path('add-staff/',views.add_staff, name='add-staff'),
    path('edit-staff/<int:pk>/',views.edit_staff, name='edit-staff' ),
    path('delete-staff/<int:pk>/',views.delete_staff, name='delete-staff' ),

     path('blogs/',views.show_blogs, name='blogs' ),
    path('add-blog/',views.add_blog, name='add-blog'),
     path('edit-blog/<int:pk>/',views.edit_blog, name='edit-blog' ),
    path('delete-blog/<int:pk>/',views.delete_blog, name='delete-blog' ),

    path('events/',views.show_events, name='events' ),
    path('add-event/',views.add_events, name='add-event'),
    path('edit-event/<int:pk>/',views.edit_event, name='edit-event' ),
    path('delete-event/<int:pk>/',views.delete_event, name='delete-event' ),


# SMS
    path('sms/', views.show_sms, name='sms'),
    path("send-sms", views.send_sms, name='send_sms')


 
]