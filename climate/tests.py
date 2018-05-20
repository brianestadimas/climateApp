from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index

# Create your tests here.
class ClimateUnitTest(TestCase):

	def test_climate_url_is_exist(self):
	    response = Client().get('/')
	    self.assertEqual(response.status_code, 200)

	def test_climate_using_index_func(self):
	    found = resolve('/')
	    self.assertEqual(found.func, index)
