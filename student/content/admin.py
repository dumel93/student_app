from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields=['first_name', 'last_name', 'school_class']

admin.site.register(SchoolSubject)
admin.site.register(StudentGrades)
