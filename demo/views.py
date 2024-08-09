from django.shortcuts import render,redirect
from .forms import UserProfile
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    data = UserProfile()
    if request.method == 'POST':
        data = UserProfile(request.POST)
        if data.is_valid():
            data.save()
            return redirect('signin')
        else:
            data = UserProfile()
    context = {'data':data}
    return render(request, 'signup.html', context)

def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')
    return render(request, 'signin.html')
