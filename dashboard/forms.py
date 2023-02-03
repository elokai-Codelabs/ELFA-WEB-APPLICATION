from django.forms import ModelForm
from django import forms
from website.models import Department

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields ='__all__'
      
       
    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


