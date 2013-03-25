from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
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
    t = loader.get_template('manage_account_login/registration.html')
    c = RequestContext(request, {'registration_form': form})
    return HttpResponse(t.render(c))
