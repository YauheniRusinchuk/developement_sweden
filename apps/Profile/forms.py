from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='',required=True,max_length=100)
    first_name = forms.CharField(label='', max_length=100)
    last_name = forms.CharField(label='', max_length=100)
    password = forms.CharField(label='',required=True,widget=forms.PasswordInput())


    username.widget.attrs.update({'placeholder': 'Username* ...'})
    password.widget.attrs.update({'placeholder': 'Password* ...'})
    first_name.widget.attrs.update({'placeholder': 'First Name ...'})
    last_name.widget.attrs.update({'placeholder': 'Last Name ...'})
