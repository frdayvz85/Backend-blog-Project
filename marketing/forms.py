from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


#import sweetify




class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)



    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Şifrenizi ve ya parolanızı yanlış girdiniz!")
            return super(LoginForm, self).clean()



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
   # email = forms.EmailField()
    password1 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Password again', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parollalar Eşleşmiyor!')
        return password2

'''
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is taken!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is taken!')
        return email
'''
    
    