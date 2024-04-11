from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView

from task_manager.mixins import MyLoginRequiredMixin, DeleteProtectedMixin
from .models import Task
from .forms import TaskForm
from .filters import TaskFilter


class ListTaskView(MyLoginRequiredMixin, FilterView):
    template_name = 'tasks/index.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    extra_context = {
        'header': _('Tasks'),
        'button_text': _('Show'),
    }


class DetailTaskView(MyLoginRequiredMixin, DetailView):
    template_name = 'tasks/task.html'
    model = Task
    context_object_name = 'task'
    extra_context = {
        'header': _('Task viewing')
    }


class CreateTaskView(MyLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    success_message = _('Task is successfully created')
    extra_context = {
        'header': _('Create task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(MyLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    success_message = _('Task is successfully changed')
    extra_context = {
        'header': _('Task change'),
        'button_text': _('Change'),
    }


class DeleteTaskView(MyLoginRequiredMixin, DeleteProtectedMixin,
                     SuccessMessageMixin, DeleteView):
    template_name = 'delete.html'
    model = Task
    success_url = reverse_lazy('task_list')
    success_message = _('Task is successfully deleted')
    author_check_message = _('The task can be deleted only by its author')
    author_check_url = reverse_lazy('task_list')
    extra_context = {
        'header': _('Delete task'),
        'button_text': _('Yes, delete'),
    }
