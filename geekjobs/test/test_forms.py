from django.test import TestCase
from geekjobs.forms import JobForm


class JobFormTestCase(TestCase):
    def setUp(self):
        self.form_data = {
            'title': 'Python dev',
            'city': 'Berlin',
            'state': 'DE',
            'remote': False,
            'description': 'Some description',
            'instructions': 'Some instructions',
            'name': 'Google',
            'url': 'http://www.url.com',
            'email': 'email@email.com'
        }

    def test_JobForm_valid(self):
        form = JobForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        form.save()

    def test_JobForm_email(self):
        self.form_data['email'] = 'aaa'
        form = JobForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_JobForm_salary(self):
        self.form_data['salary'] = 'Some salary.'
        form = JobForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        form.save()
        self.form_data['salary'] = None
        form = JobForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        form.save()

    def test_JobForm_valid(self):
        form = JobForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        form.save()

