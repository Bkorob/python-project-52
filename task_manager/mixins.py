from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class MyLoginRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,
                           _('You are not logged in! Please log in.'))
            return redirect(reverse_lazy('login'))

        return super().dispatch(request, *args, **kwargs)


class CheckUserMixin(UserPassesTestMixin):
    permission_message = None
    permission_url = None

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)


class DeleteProtectedMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
