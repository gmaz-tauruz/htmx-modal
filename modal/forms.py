from datetime import datetime
from random import choices
from django import forms

from .models import Employee


# class DateInput(forms.DateInput):
#     input_type ='date'
    

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'middle_name', 'birth_date',
            'gender', 'description',
        ]

        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 
                'max': datetime.now().date()}),
            'gender': forms.Select(),            
            'description': forms.Textarea(),
                # From Bootstrap5 Floating-labels: 
                # To set a custom height on your <textarea>, do not use the rows attribute. 
                # Instead, set an explicit height (either inline or via custom CSS).
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['gender'].empty_label = "None"