from django import forms
from django.contrib.auth.models import User

from users.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'last_name', 'first_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name'}

    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match!')
        return self.cleaned_data['password2']
