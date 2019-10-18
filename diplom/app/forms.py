from django import forms
from .admin import UserCreationForm
from .models import MyUser


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if MyUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email


