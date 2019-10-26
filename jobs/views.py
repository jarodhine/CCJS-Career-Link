from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
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

@login_required(login_url='login_url')
def dashboardView(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='jobs/login')
def profileView(request):
    return render(request, 'profile.html')

@login_required(login_url='jobs/login')
def jobSearchView(request):
    return render(request, 'jobSearch.html')

@login_required(login_url='jobs/login')
def profileSearchView(request):
    return render(request, 'profileSearch.html')

class PostListView(ListView):
    model = Post
    template_name = 'dashboard.html'
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'requirements', 'description']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)