from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import MyLoginRequiredMixin, DeleteProtectedMixin
from .models import Label
from .forms import LabelForm


class ListLabelView(MyLoginRequiredMixin, View):
    template_name = 'labels/index.html'

    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request, self.template_name, {"labels": labels, 'header': _('Labels')})


class CreateLabelView(MyLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('label_list')
    success_message = _('Label is successfully created')
    extra_context = {
        'header': _('Create label'),
        'button_text': _('Create'),
    }


class UpdateLabelView(MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('label_list')
    success_message = _('Label is successfully changed')
    extra_context = {
        'header': _('Change label'),
        'button_text': _('Change'),
    }


class DeleteLabelView(MyLoginRequiredMixin, DeleteProtectedMixin,
                      SuccessMessageMixin, DeleteView):
    template_name = 'delete.html'
    model = Label
    success_url = reverse_lazy('label_list')
    success_message = _('Label is successfully deleted')
    protected_message = _('Unable to delete a label because it is in use')
    protected_url = reverse_lazy('label_list')
    extra_context = {
        'header': _('Delete label'),
        'button_text': _('Yes, delete'),
    }
