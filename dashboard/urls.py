from django.urls import path
from .import views 
urlpatterns = [
    path('',views.dashboard, name='dashboard' ),
    path('details/',views.school_info, name='info' ),
    path('show-departments/',views.show_departments, name='show-departments' ),
    path('add-departments/',views.add_department, name='add-departments' ),
 
]