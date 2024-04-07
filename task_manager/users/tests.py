from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class CustomUserCRUDTest(TestCase):
    def setUp(self):
        self.test_model = CustomUser.objects.create(
            first_name='TestFirst_name', 
            last_name = 'TestLast_name',
            username = 'TestUser_name',
        )
    def test_create(self):
        response = self.client.post(
            reverse('user_create'), {
                'first_name': 'TestFirst_n', 
                'last_name': 'TestLast_n',
                'username': 'TestUser_n',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(CustomUser.objects.filter(first_name='TestFirst_n').exists())

    def test_read(self):
        response = self.client.get(reverse('detail_url', kwargs={'pk': self.your_model.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.your_model.name)

    def test_update(self):
        response = self.client.post(reverse('update_url', kwargs={'pk': self.your_model.pk}), {'name': 'Updated Test Name', 'description': 'Updated Test Description'})
        self.assertEqual(response.status_code, 200)
        self.your_model.refresh_from_db()
        self.assertEqual(self.your_model.name, 'Updated Test Name')

    def test_delete(self):
        response = self.client.post(reverse('delete_url', kwargs={'pk': self.your_model.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(YourModel.objects.filter(pk=self.your_model.pk).exists())