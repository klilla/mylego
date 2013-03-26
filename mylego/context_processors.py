from django.forms import forms

__author__ = 'kasia'


def login_form(request):
    from django.contrib.auth.forms import AuthenticationForm
    login_form = AuthenticationForm()
    login_form.fields['username'].widget.attrs = {'class':'span2', 'placeholder':'Username'}
    login_form.fields['password'].widget.attrs = {'class':'span2', 'placeholder':'Password'}
    return {'login_form': login_form}