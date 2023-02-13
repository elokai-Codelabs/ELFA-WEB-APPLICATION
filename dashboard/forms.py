from django.forms import ModelForm
from django import forms
from website.models import Department,Team_Member,Staff,Event,Blog
from django.core.exceptions import ValidationError
from django.utils import timezone


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields ='__all__'

    def clean_name_of_department(self):
        name = self.cleaned_data['name_of_department']
        if Department.objects.filter(name_of_department=name).exists():
            raise ValidationError("Department with this name already exists.")
        return name 
       
    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class TeamForm(ModelForm):
    class Meta:
        model = Team_Member
        fields ='__all__'

    
    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class StaffForm(ModelForm):
    now = timezone.now()
    formatted_date = now.strftime('%Y-%m-%d')
    date_of_assumption = forms.DateField(label=f'Date Started (yyyy-mm-dd) e.g ({formatted_date})')
    class Meta:
        model = Staff
        fields ='__all__'
    
    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields ='__all__'

    
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ='__all__'

    
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

