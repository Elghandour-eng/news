from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm

from .models import CustomUser


class CustomUserCreationform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        Model = CustomUser
        fields = UserChangeForm.Meta.fields        