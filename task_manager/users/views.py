from django.shortcuts import render
from django.views.generic import(
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
)


# Create your views here.
class IndexUsers(ListView):
    pass


class UpdateUser(UpdateView):
    pass


class CreateUser(CreateView):
    pass


class DeleteUser(DeleteView):
    pass
