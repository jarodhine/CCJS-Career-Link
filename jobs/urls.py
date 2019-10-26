from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name="home_url"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='dashboard_url'), name="logout_url"),
    path('dashboard/', PostListView.as_view(), name="dashboard_url"),
    path('profile/', views.profileView, name="profile_url"),
    path('jobsearch/', views.jobSearchView, name="jobSearch_url"),
    path('profilesearch/', views.profileSearchView, name="profileSearch_url"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="detail_url"),
    path('post/new/', PostCreateView.as_view(), name="create_url"),
]