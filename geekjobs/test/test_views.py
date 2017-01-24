from django.test import RequestFactory
from django.test import TestCase
from geekjobs.stackoverflow_parser import eu_countries_sorted
from django.test.utils import setup_test_environment
from django.utils.translation import activate
from django.core.urlresolvers import reverse
from geekjobs.views import *

request_factory = RequestFactory()


class ViewsTestCase(TestCase):
    def test_index(self):
        """test index view"""
        response = self.client.get('/', follow=True)
        self.assertRedirects(response, response.redirect_chain[0][0])
        for k, v in eu_countries_sorted.items():
            response = self.client.get('/'+k, follow=True)
            self.assertRedirects(response, response.redirect_chain[0][0])

    def test_pricavy(self):
        """test privacy view"""
        response = self.client.get('/privacy', follow=True)
        self.assertRedirects(response, response.redirect_chain[0][0])

    def test_terms(self):
        """test terms view"""
        response = self.client.get('/terms', follow=True)
        self.assertRedirects(response, response.redirect_chain[0][0])

    def test_new(self):
        """test new view"""
        response = self.client.get('/new', follow=True)
        self.assertRedirects(response, response.redirect_chain[0][0])
        response = self.client.post('/new', follow=True)
        self.assertRedirects(response, response.redirect_chain[0][0])

    def test_add_jobs(self):
        """test add_jobs view method"""
        response = self.client.get('/add_job', follow=True)
        self.assertRedirects(response, response.redirect_chain[0][0])
        response = self.client.post('/add_job', follow=True)
        self.assertRedirects(response, response.redirect_chain[0][0])

