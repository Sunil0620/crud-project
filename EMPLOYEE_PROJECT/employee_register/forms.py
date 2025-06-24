from django import forms
from .models import Employee
class Form(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('full_name', 'mobile_number', 'employee_code', 'position')
        labels = {
            'full_name': 'Full Name',
            'mobile_number': 'Mobile',
            'employee_code' : 'EMP. Code',
            'position' : 'Position'
        }
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['employee_code'].required = False  # Not mandatory
