from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    MyLoginRequiredMixin,
    SelfCheckUserMixin,
    CanDeleteProtectedEntityMixin,
)
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserUpdateForm

# Create your views here.
class UsersListView(View):

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, 'users/index.html', {'users': users})

class UpdateUserView(MyLoginRequiredMixin, SelfCheckUserMixin,
                     SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = CustomUser
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')
    extra_context = {
        'header': _('Update user'),
        'button_text': _('Update'),
    }


class CreateUserView(SuccessMessageMixin, CreateView):
    
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')
    success_message = _('User is created successfully')
    extra_context = {
        'header': _('Registration'),
        'button_text': _('Register '),
    }


class DeleteUserView(MyLoginRequiredMixin, SelfCheckUserMixin,
                     CanDeleteProtectedEntityMixin,
                     SuccessMessageMixin, DeleteView):
    
    template_name = 'delete.html'
    model = CustomUser
    success_url = reverse_lazy('users')
    success_message = _('User is successfully deleted')
    permission_message = _('You have no rights to delete another user.')
    permission_url = reverse_lazy('users')
    protected_message = _('Unable to delete a user because he is in use')
    protected_url = reverse_lazy('users')
    extra_context = {
        'header': _('Deleting user'),
        'button_text': _('Yes, delete'),
    }
