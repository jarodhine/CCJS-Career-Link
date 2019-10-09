from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.http import HttpResponse

# Create your views here.

# for index pages

def indexView(request):
    return render(request, 'index.html')

def searchView(request):
    return render(request, "search.html")

def sprofileView(request):
    return render(request, "student-profile.html")

def pprofileView(request):
    return render(request, "professor-profile.html")

def eprofileView(request):
    return render(request, "employer-profile.html")

def uprofileView(request):
    return render(request, "unspecified-profile.html")




# end this line



@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

@login_required
def accountView(request):
    return render(request, 'account.html')

def registerView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form':form})
