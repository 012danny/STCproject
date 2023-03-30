from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
	path('signup/', views.signup, name= 'signup'),
	path('signout/', views.signout, name= 'signout'),
	path('signin/', views.signin, name= 'signin'),
	path('profile/', views.profile, name= 'profile'),
	path('newtrip/', views.newtrip, name= 'newtrip'),
	path('mystringer/', views.mystringer, name= 'mystringer'),
]