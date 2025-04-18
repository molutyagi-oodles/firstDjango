from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
            'placeholder': 'Enter subject'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
            'placeholder': 'Enter your email'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
            'placeholder': 'Write your message here...',
            'rows': 5
        })
    )


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
            'placeholder': 'Enter password'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
                'placeholder': 'Email address'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-3 border-4 border-red-400 rounded-lg bg-white text-gray-900',
            'placeholder': 'Enter your password'
        })
    )