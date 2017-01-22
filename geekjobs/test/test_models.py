from datetime import datetime
from time import struct_time

from django.test import TestCase
from geekjobs.models import Job
from geekjobs.models import load_model_jobs


class JobTestCase(TestCase):
    def setUp(self):
        """Creates a single object for testing purposes"""
        Job.objects.create(title="Python dev",
                           city="Berlin",
                           state='DE',
                           description="Some description",
                           instructions="Some instructions",
                           name="Company name",
                           url="http://www.url.com",
                           email="email@email.com")

    def test_default_fields(self):
        """Jobs default field are correctly"""
        job = Job.objects.get(title="Python dev")
        self.assertEqual(job.remote, False)
        self.assertIs(job.salary, None)
        self.assertIsInstance(job.published, datetime)

    def test_load_model_jobs(self):
        """Check loading jobs from database and converting them to jobItem"""
        jobs = load_model_jobs()
        self.assertEqual(len(jobs['DE']), len(jobs['EU']))
        self.assertEqual(len(jobs['DE']), 1)
        self.assertEqual(len(jobs['REMOTE']), 0)

        job = jobs['DE'][0]
        self.assertEqual(job['title'], 'Python dev at Company name (Berlin , Germany)')
        self.assertEqual(job['summary'], 'Some description')
        self.assertEqual(job['featured'], True)
        self.assertEqual(job['link'], 'http://www.url.com')
        self.assertEqual(job['instructions'], 'Some instructions')
        self.assertEqual(job['author'], 'Company name')
        self.assertIsInstance(job['updated_parsed'], struct_time)
        self.assertEqual(job['location'], '')
        self.assertEqual(job['published'], '')
        self.assertEqual(job['days'], 0.0)
