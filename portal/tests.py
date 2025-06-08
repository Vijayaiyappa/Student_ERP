import json
from django.test import TestCase, Client
from django.contrib.auth.models import User
from . import models  # Make sure this points to your app's models

class StudentIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_add_student_via_ajax(self):
        response = self.client.post(
            '/save_ajax/',
            content_type='application/json',
            data=json.dumps({
                'name': 'Alice',
                'subject': 'Science',
                'marks': 75
            })
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(models.Student.objects.filter(name='Alice', subject='Science').exists())

