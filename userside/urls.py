from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('auth',views.authentication,name='authentication'),
    path('slist',views.studentlist.as_view(),name='s1'),
]