from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import SCHOOL_CLASS, Student
from accounts.models import User
from .validators import validate_year_of_birth, validate_year_length


class StudentSearchForm(forms.Form):
    last_name = forms.CharField(max_length=3)



