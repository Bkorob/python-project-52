from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].requred = True

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2'
                  ]
        

class CustomUserUpdateForm(UserCreationForm):

    def clean_username(self):
        return self.cleaned_data.get("username")
