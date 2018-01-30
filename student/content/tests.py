
from django.test.client import Client
import unittest
from django.test import TestCase

from .models import Student,SCHOOL_CLASS


def get_school_class(class_id):
    for item in SCHOOL_CLASS:
        if item[0] == class_id:
            return item

class StudentTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.student = Student.objects.create(first_name ='Adrian',
                                              last_name="Strzępek",
                                              school_class=1,
                                              year_of_birth=int('1995'),
                                              )

    def tearDown(self):
        self.student = None

    def test_student(self):
        self.assertEqual(self.student.first_name, 'Adrian')
        self.assertEqual(self.student.last_name, 'Strzępek')
        self.assertEqual(get_school_class(1)[1], "1UID-1")
        self.assertEqual(self.student.year_of_birth, 1995)

    def test_student_details(self):
        # Issue a GET request.
        response = self.client.get('/content/class/1')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 student.
        self.assertEqual(len(response.context['students']), 1)


    def test_student_delete(self):
        response1 = self.client.get('/content/student/1')
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.get('/content/delete/1/')
        self.assertEqual(response2.status_code, 200)
        response3 = self.client.post('/content/delete/1')
        self.assertEqual(response3.status_code, 301)

    def test_student_edit(self):
        response1 = self.client.get('/content/student/1')
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.get('/content/edit/1/')
        self.assertEqual(response2.status_code, 200)
        response3 = self.client.post('/content/edit/1',{'year_of_birth': 1990})
        self.assertEqual(response3.status_code, 301)



