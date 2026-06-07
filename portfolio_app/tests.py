from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
	def test_index_status_code_and_template(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')
		self.assertContains(response, 'Welcome to your portfolio site!')
