import logging

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm, AccountAuthenticationForm
from django.contrib import messages

logger = logging.getLogger(__name__)

def home(request):

    return render(request, 'home.html')


def signup(request):
    context = {}
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            logger.info('User signed up successfully')
            return redirect('home')
        else:
            context['sign_up_form'] = form
    else:
        form = SignUpForm()
        context['sign_up_form'] = form
    return render(request, 'signup.html', context)


def logout_view(request):
    logout(request)
    logger.info('User logged out')
    return redirect('home')


import logging

logger = logging.getLogger(__name__)


from django.contrib.auth import get_user_model
User = get_user_model()
def login_view(request):
    if request.method == 'POST':
        login_form = AccountAuthenticationForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.filter(email=email).first()
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials')
    else:
        login_form = AccountAuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})



