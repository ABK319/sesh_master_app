import os 
import django
from django.contrib.auth.models import User
from seshmaster.models import Nightclub
import populate.py
from django.test import TestCase

		

class NightclubMethodTests(TestCase):
	def test_reviews_are_positive(self):
	
		#should return true if the average score for a given nightclub is positive
		rev = Nightclub(name="test", average_score="-1")
		rev.save()
		self.assertEqual((rev.average_score >= 1), True)

		
	def test_population_script_works(self):
		
	