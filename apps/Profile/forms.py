from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='',required=True,max_length=100)
    first_name = forms.CharField(label='', max_length=100)
    last_name = forms.CharField(label='', max_length=100)
    password = forms.CharField(label='',required=True,widget=forms.PasswordInput())


    username.widget.attrs.update({'placeholder': 'Username* ...', 'class' : 'registration_username_form'})
    password.widget.attrs.update({'placeholder': 'Password* ...', 'class' : 'registration_password_form'})
    first_name.widget.attrs.update({'placeholder': 'First Name ...', 'class' : 'registration_firstname_form'})
    last_name.widget.attrs.update({'placeholder': 'Last Name ...', 'class' : 'registration_lastname_form'})
