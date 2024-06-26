from django.test import TestCase
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status
from task_manager.users.models import CustomUser as User


class StatusCrudTestCase(TestCase):

    fixtures = ["users", "statuses"]

    def setUp(self):
        self.users = User.objects.all()
        self.client.force_login(self.users[0])
        self.statuses = Status.objects.all()
        self.test_statuses = {"name": "status4"}

    def test_create_status(self):

        response = self.client.get(reverse_lazy('status_create'))
        self.assertContains(response, _('Create status'), status_code=200)

        response = self.client.post(
            reverse_lazy('status_create'),
            self.test_statuses,
            follow=True
        )
        self.assertContains(response, _('Status is successfully created'), status_code=200)
        self.assertTrue(Status.objects.filter(name=self.test_statuses["name"]).exists())

    def test_update_status(self):

        status1 = self.statuses[0]
        request_url = reverse_lazy('status_update', kwargs={'pk': status1.pk})
        new_name = 'changed'
        response = self.client.post(
            request_url,
            {
                'name': new_name
            },
            follow=True
        )
        self.assertContains(response, _('Status is successfully changed'), status_code=200)
        self.assertTrue(Status.objects.filter(name=new_name).exists())

    def test_delete_status_success(self):

        status3 = self.statuses[2]
        request_url = reverse_lazy('status_delete', kwargs={'pk': status3.pk})
        name_deleted = status3.name
        response = self.client.post(request_url, follow=True)
        self.assertContains(response, _('Status is successfully deleted'), status_code=200)
        self.assertFalse(
            Status.objects.filter(name=name_deleted).exists()
        )

    def test_get_all_statuses(self):

        response = self.client.get(reverse_lazy('status_list'))
        for status in self.statuses:
            self.assertContains(response, status.name)
