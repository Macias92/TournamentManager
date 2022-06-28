from django import forms


class LoginForm(forms.Form):  # Form connected with login
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreateUserForm(forms.Form):  # Form allows to create a new user
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


