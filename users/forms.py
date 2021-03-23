from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserOurregistration(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password1 = forms.CharField(required=False)
    slug = forms.CharField(required=False)
    long_links = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['username', 'password1', 'slug', 'long_links']