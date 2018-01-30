from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from .validators import validate_year_length, validate_year_of_birth


SCHOOL_CLASS = [
    (1, "1UID-1"),
    (2, "1UID-2"),
    (3, "2UID-3"),
    (4, "2UID-4"),
]

GRADES = (

    (3.0, "3"),
    (3.5, "3.5"),
    (4.0, "4"),
    (4.5, "4.5"),
    (5.0, "5"),

)



# Create your models here.
class SchoolSubject(models.Model):
    name = models.CharField(max_length=64)
    teacher_name = models.CharField(max_length=64)

    def __str__(self):
        return self.name



class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name =  models.CharField(max_length=64)
    school_class = models.IntegerField(choices=SCHOOL_CLASS)
    grades = models.ManyToManyField(SchoolSubject, through="StudentGrades")
    year_of_birth=models.IntegerField(null=True, validators=[validate_year_length, validate_year_of_birth])


    def get_absolute_url(self):
        return reverse('content:student', kwargs={'student_id': self.id})

    def get_edit_url(self):
        return reverse('content:edit', kwargs={'student_id': self.id})

    def get_delete_url(self):
        return reverse('content:delete',kwargs ={'student_id': self.id})


    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class StudentGrades(models.Model):
    student = models.ForeignKey(Student)
    school_subject = models.ForeignKey(SchoolSubject)
    grade = models.FloatField(choices=GRADES)

    def __str__(self):
        return '{} - {} : {}'.format(self.student,self.school_subject,self.grade)
