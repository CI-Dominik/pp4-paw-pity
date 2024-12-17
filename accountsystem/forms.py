from django.contrib.auth.forms import AuthenticationForm
from django import forms
from main.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomLoginForm(AuthenticationForm):

    class Meta:
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=30,
        help_text='Required. 30 characters or fewer.'
        )
    username = forms.CharField(
        max_length=15,
        help_text='''Required. 15 characters or fewer. Letters, '''
        '''digits and @/./+/-/_ only.'''
        )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email is already taken. Please choose a different one."
                )
        return email

    def clean_username(self):
        original_username = self.cleaned_data.get('username')
        username = original_username.lower()
        existing_user = CustomUser.objects.filter(username__iexact=username).first()
        if existing_user:
            raise forms.ValidationError(
                "This username is already taken."
            )
        return original_username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "The passwords do not match. Please try again."
                )
        return password2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
