from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext


def registration(request):
    if request.method == 'POST':
        print 'POST'
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            print form.cleaned_data['username']
            form.save()
            pd = form.cleaned_data['password1']
            un = form.cleaned_data['username']
            user = authenticate(username=un, password=pd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    t = loader.get_template('pages_static/index.html')
                    c = RequestContext(request, {})
                    return HttpResponse(t.render(c))
        else:
            print 'Some error'
            print form.is_valid()
    else:
        form = UserCreationForm()
    t = loader.get_template('user_authentication/registration.html')
    c = RequestContext(request, {'registration_form': form})
    return HttpResponse(t.render(c))

def log_in(request):
    message = ''
    if request.method == 'POST':
        print 'POST'
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            pd = form.cleaned_data['password']
            un = form.cleaned_data['username']
            user = authenticate(username=un, password=pd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    #return HttpResponseRedirect(reverse('index'))
                    t = loader.get_template('pages_static/index.html')
                    c = RequestContext(request, {'login_form': form, 'message': message})
                    return HttpResponse(t.render(c))
                else:
                    message = 'Your account is disabled. Contact with administrator.'
            # Return a 'disabled account' error message
            else:
                message = 'Your login or password is invalid. Check twice.'
                # Return an 'invalid login' error message.
        else:
            message = ''
    else:
        form = AuthenticationForm()
    t = loader.get_template('user_authentication/login.html')
    c = RequestContext(request, {'login_form': form, 'message': message})
    return HttpResponse(t.render(c))

def logging_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
