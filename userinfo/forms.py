from django import forms
from userinfo.models import User
from datetime import date


# class DateInput(forms.DateInput):
#      input_type='date'

class UserForm(forms.ModelForm):
    def clean_birthday(self):
        dob = self.cleaned_data['dob']
        age = (date.today() - dob).days / 365
        if age < 18:
            raise forms.ValidationError('You must be at least 18 years old')
        return dob

    class Meta:
        model = User
        fields = [
            'name', 'dob', 'email', 'phone',
        ]
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={ 'type':'date','class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
        }


