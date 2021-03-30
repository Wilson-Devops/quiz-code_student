from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name="HomePage"),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('register/',views.register,name='register'),
    path('quiz/',views.quiz,name='quiz')
    
    

]