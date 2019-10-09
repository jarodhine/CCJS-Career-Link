from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin

urlpatterns = [
    path('', views.indexView, name="index_url"),
    path('search/', views.searchView, name="search_url"),
    path('student-profile/', views.sprofileView, name="student-profile_url"),
    path('professor-profile/', views.pprofileView, name="professor-profile_url"),
    path('employer-profile/', views.eprofileView, name="employer-profile_url"),
    path('unspecified-profile/', views.uprofileView, name="unspecified-profile_url"),


    path('dashboard/', views.dashboardView, name="dashboard_url"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='dashboard_url'), name="logout_url"),
#     path('index/', view.index, name= 'index')
]