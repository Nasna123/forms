from django.urls import path
from.import views

urlpatterns=[
    path('page1/',views.fun1,name='page1'),
     path('homeform/',views.homeform,name='homeform'),
    path('loginform/',views.loginform,name='loginform'),
    path('signupform/',views.signupform,name='signupform'),
]