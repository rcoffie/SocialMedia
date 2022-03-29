from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError 
from django.forms.fields import EmailField
from django.forms import Form


class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=30, required=False, help_text='Opitonal')
  last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
  email = forms.EmailField(max_length=255, help_text='Required, inform a valid email address. ')

  class Meta:
    model = User 
    fields = ('username','first_name','last_name','password1','password2')

  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        # self.fields['comment'].widget.attrs.update(size='40')
        self.fields['first_name'].widget.attrs.update({'class':'form-control'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})