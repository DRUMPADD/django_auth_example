from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'auth/home.html')

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})