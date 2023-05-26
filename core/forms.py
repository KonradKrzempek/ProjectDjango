from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text="Required. Insert a valid email address")
    date_of_birth = forms.DateField(input_formats=('%d-%m-%Y', '%Y-%m-%d'), help_text="DD-MM-YY format")
    street = forms.CharField(max_length=50)
    post_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=30)
    country = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'email',
                  'street', 'city', 'post_code', 'country')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        # Get the user with the given email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("Invalid login")

        # Check if the password is correct
        if not check_password(password, user.password):
            raise forms.ValidationError("Invalid login")

        return self.cleaned_data