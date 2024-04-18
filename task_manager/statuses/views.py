from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from task_manager.mixins import MyLoginRequiredMixin, DeleteProtectedMixin
from .models import Status
from django.contrib.messages.views import SuccessMessageMixin
from .forms import StatusForm


class ListStatusView(MyLoginRequiredMixin, View):
    template_name = 'statuses/index.html'

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, self.template_name, {"statuses": statuses, 'header': _('Statuses')})


class CreateStatusView(MyLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('status_list')
    success_message = _('Status is successfully created')
    extra_context = {
        'header': _('Create status'),
        'button_text': _('Create'),
    }


class UpdateStatusView(MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('status_list')
    success_message = _('Status is successfully changed')
    extra_context = {
        'header': _('Change status'),
        'button_text': _('Change'),
    }


class DeleteStatusView(MyLoginRequiredMixin, DeleteProtectedMixin,
                       SuccessMessageMixin, DeleteView):
    template_name = 'delete.html'
    model = Status
    success_url = reverse_lazy('status_list')
    success_message = _('Status is successfully deleted')
    protected_message = _('Unable to delete a status because it is in use')
    protected_url = reverse_lazy('status_list')
    extra_context = {
        'header': _('Delete status'),
        'button_text': _('Yes, delete'),
    }
