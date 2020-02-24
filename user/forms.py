from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from .choices import USER_TYPE_CHOICES

class CustomUserCreationForm(UserCreationForm):
    avatar = forms.FileField(required=False, widget=forms.FileInput(attrs={'accept':'image/*'}))
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name',)



#### more
# https://medium.com/@gajeshbhat/extending-and-customizing-django-allauth-eed206623a1a