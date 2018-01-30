from django.test import TestCase
from django.test.client import Client
# Create your tests here.
import unittest
from .models import User




class AdminTestCase(TestCase):

    def setUp(self):
        self.admin =User.objects.create_superuser('admin',
                                                  'admin@wp.pl',
                                                  'test1234')
        self.client = Client()

    def test_admin_login(self):
        # Get login page
        response = self.client.get('/admin/login/')

        # Check response code
        self.assertEquals(response.status_code, 200)

        # Log the admin in
        self.client.post('/admin/login/')
        self.client.login(username='admin ', password="test1234")
        response = self.client.post('/admin/login/')
        self.assertEquals(response.status_code, 200)

    def test_admin_logout(self):
        # Log in
        self.client.login(username='admin', password="admin123")

        # Check response code
        response = self.client.get('/admin/login/')
        self.assertEquals(response.status_code, 200)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 302)



class UserTestCase(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create(username='dumel0', email='test@wp.pl',password="test123")
        self.user.save()



    def tearDown(self):
        self.user =None


    def test_user_name(self):
        self.assertEqual(self.user.username, "dumel0")

    def test_signup(self):
        response=self.client.post('/accounts/signup/',
                                    {'username': 'dumel0',
                                     'email': 'test@wp.pl',
                                     'password1': 'test123',
                                     'password2': 'test123'}
                                    )


        self.assertEqual(response.status_code, 200)


    def test_login(self):
         self.client.post('/accounts/login',
                                    {'username': 'dumel0',
                                     'password': 'test123',
                                     }
                                    )
         response=self.client.get('/log/')

         self.assertEqual(response.status_code, 200)



    def test_logout(self):
        self.client.post('/accounts/login',
                         {'username': 'dumel0',
                          'password': 'test123',
                          }
                         )
        self.client.logout()

        response = self.client.get('/thanks/')
        self.assertEquals(response.status_code, 200)


class PageTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)




