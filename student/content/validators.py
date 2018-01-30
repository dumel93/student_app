from django import forms

def validate_year_of_birth(value):
    if int(value) >= 1998 or int(value) <=1980:
        raise forms.ValidationError('It is not a student\'s age, try again. (hint: 1980-1998)' )

def validate_year_length(value):
    if len(str(value)) != 4:
        raise forms.ValidationError('Wrong date, try again. ')
