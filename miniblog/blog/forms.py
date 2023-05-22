from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import PostModel

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # userperm = forms.ChoiceField(label="User Type",choices=(('admin','admin'),('author','author'),('subscriber','subscriber')), 
    #                              widget=forms.Select(attrs={'class':'btn btn-light dropdown-toggle text-dark col-sm-3 mx-4 mt-2'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
    password = forms.CharField(label=_('Password'),strip=False,
                               widget=forms.PasswordInput
                               (attrs={'class':'form-control','autocomplete':'current-password'}))
    
class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = "__all__"
        labels = {'title':'Title','desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'desc':forms.Textarea(attrs={'class':'form-control'}),
                   }
    
