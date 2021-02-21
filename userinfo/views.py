from django.http import response, HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from userinfo.models import User
from datetime import date


# Create your views here.


def index(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            dm = fm.cleaned_data['dob']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['phone']
            def clean_birthday(self):
                dob = self.cleaned_data['dob']
                age = (date.today() - dob).days / 365
                if age < 18:
                    raise fm.ValidationError('You must be at least 18 years old')
                return dob
            reg = User(name=nm, dob=dm, email=em, phone=pm)
            reg.save()
            fm = UserForm()
    else:
        fm = UserForm()
        stud = User.objects.all()
    stud = User.objects.all()
    return render(request, 'index.html', { 'stu': stud,'form': fm})

def clean_birthday(self):
        dob = self.cleaned_data['dob']
        age = (date.today() - dob).days / 365
        if age < 18:
            raise forms.ValidationError('You must be at least 18 years old')
        return dob
