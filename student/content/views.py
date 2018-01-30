from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import SCHOOL_CLASS, Student, SchoolSubject, StudentGrades
from django.db.models import Avg
from .forms import StudentSearchForm
from django.views.generic.edit import (FormView, CreateView, UpdateView, DeleteView)
from django.views.generic.list import (ListView, )
from django.core.exceptions import PermissionDenied
from accounts.models import User

# Create your views here.
class SchoolView(View):
    def get(self, request):
        ctx = {
            'class_list': SCHOOL_CLASS
        }
        return render(request, 'content/school.view.html', ctx)


def get_school_class(class_id):
    for item in SCHOOL_CLASS:
        if item[0] == class_id:
            return item


class SchoolClassView(View):
    def get(self, request, school_class_id):
        school_class_id = int(school_class_id)
        students = Student.objects.filter(school_class=school_class_id).order_by("last_name")
        school_class = get_school_class(school_class_id)

        return render(request, "content/class.html", {"students": students,
                                                        "class_name": school_class[1]})


class StudentInfo(View):
    def get(self, request, student_id):
        student_id = int(student_id)
        student = Student.objects.get(pk=student_id)
        school_class = get_school_class(student.school_class)
        school_subjects = SchoolSubject.objects.all()
        return render(request, "content/student.html", {"student": student,
                                                          "class_name": school_class[1],
                                                          "subjects": school_subjects}

                      )


class GradesView(View,LoginRequiredMixin):

#    login_url = '/admin/login'
 #   permission_required= ['content.add_studentgrades']           # nazwa aplikacji co chcemy robic i na czym(model_malelitery)
  #  raise_exception = True

    def get(self, request, student_id, subject_id):
        student = Student.objects.get(id=student_id)
        school_class = get_school_class(student.school_class)
        subject = SchoolSubject.objects.get(id=subject_id)
        grades = StudentGrades.objects.filter(student=student,
                                              school_subject=subject)
        avg = grades.aggregate(grade_avg=Avg('grade'))

        ctx = {'student': student,
               'subject': subject,
               'grades': grades,
               'class_name': school_class[1],
               'grades_avg': avg['grade_avg']

               }
        return render(request, 'content/grades.html', ctx)


class StudentSearchView(FormView):
    form_class = StudentSearchForm
    model_class = Student
    template_name = 'content/student_form.html'
    results_template_name = 'content/result.html'
    lookup_field = 'last_name'

    def form_valid(self, form):
        last_name = form.cleaned_data['last_name']
        results = self.model_class.objects.filter(**{
            '{}__icontains'.format(self.lookup_field): last_name
        }).order_by(self.lookup_field)
        ctx = {'results': results,
               'form': self.form_class()}
        return render(
            self.request,
            self.results_template_name,
            ctx
        )


class StudentAddView(LoginRequiredMixin,CreateView):

    template_name = 'content/student_add.html'
    model = Student
    fields = ['first_name', 'last_name', 'school_class', 'year_of_birth']






class EditView(UpdateView):

    model = Student
    fields = ['first_name', 'last_name', 'school_class', 'year_of_birth']
    template_name = "content/student_edit.html"  # update_form.html



class DeleteView(DeleteView):
    model = Student
    success_url = '/'
    template_name="content/student_confirm_delete.html"   #lub nie musze ale musi byc: _confirm_delete.html


class ListUsersView(ListView):
    model = User



