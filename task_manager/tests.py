from django.test import Client, TestCase
from django.shortcuts import reverse


class HomePageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
