from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Post

# Create your views here.

posts = [
    {
        'title': 'System Technician',
        'requirements': 'Bachelors',
        'description': 'Entry level technician working on retail database.',
        'date': 'January 1, 2019',
        'author': 'john doe'
    },
    {
        'title': 'System Technician',
        'requirements': 'Bachelors',
        'description': 'Entry level technician working on retail database.',
        'date': 'January 1, 2019',
        'author': 'john doe'
    },
    {
        'title': 'System Technician',
        'requirements': 'Bachelors',
        'description': 'Entry level technician working on retail database.',
        'date': 'January 1, 2019',
        'author': 'john doe'
    }
]

def indexView(request):
    return render(request, 'index.html')

def registerView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form':form})

@login_required(login_url='jobs/login')
def dashboardView(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='jobs/login')
def profileView(request):
    return render(request, 'profile.html')

@login_required(login_url='jobs/login')
def searchView(request):
    return render(request, 'search.html')
