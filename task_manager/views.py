from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    return render(request, 'home.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('home')
    extra_context = {
        'header': _('Login'),
        'button_text': _('Enter'),
    }
    success_message = _('You are logged in')


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        # Добавляем сообщение о выходе пользователя
        messages.info(request, _('You are logged out'))
        # Вызываем стандартный метод выхода пользователя
        return redirect(reverse_lazy('home'))
