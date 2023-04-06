from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.forms import newtripform
from home.models import posts, AuthUser
from django.contrib.sessions.models import Session



#view for the users profile page
def profile(request):
	logs = posts.objects.all()
	return render(request,'profile.html',{'logs':logs})

#sign up page view grabing pre-consturcted form/function from django lib "UsderCreationForm"
def signup(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')         # grabs the entered username from the form
			password = form.cleaned_data.get('password1')        # grabs the password from the form 
			user = authenticate(username=username, password=password) # passes username and password to be authenicated by django lib
			login(request, user)
			return redirect('/')
		else:
			return render(request,'signup.html', {'form': form})  # renders the signup.html with the errors returned form the django lib
	else:
		form = UserCreationForm()
		return render(request, 'signup.html', {'form': form})





#view for home page where users will be welcomed "index.html"
def landingpage(request):
    return render(request,'landingpage.html',{})



#view for the add new trip page
def newtrip(request):
	form = newtripform(request.POST)
	if request.method == 'POST' :		
		if form.is_valid():
			form.save()
			title = form.cleaned_data.get('title')
			content = form.cleaned_data.get('content')
			userid = request.User.id 
			form = newtripform(request, title=title, content=content, userid=userid)	
			return redirect('/profile',{'form': form})

		
	else:
		return render(request,'newtrip.html',{'form': form})





#view for the stringer page
def mystringer(request):
    return render(request,'mystringer.html',{})



#edit a post from the DB


def edit(request):
	return render(request,'edit.html')







def delete(request):
	return render(request,'delete.html')








#sign In view to log the user in and to the profile page

def signin(request):
	if request.user.is_authenticated:
		return render(request, 'landingpage.html')
	if request.method == 'POST':
		username = request.POST['username']     #grabbing the username and password from user 
		password = request.POST['password']
		user = authenticate(request, username=username, password=password) #authenticating user with django lib
		if user is not None:
			login(request, user)
			return redirect('/profile')  	# if successful authentication send user to profile page.
		else:
			msg = 'Login Error'  		 #if error in authentication let them try agian and display login error.
			form = AuthenticationForm(request.POST)
			return render(request, 'login.html', {'form' : form, 'msg': msg})	
	else:
		form = AuthenticationForm()
		return render(request, 'login.html', {'form': form})







#Logout view to log the user out and back to home page


def signout(request):
	logout(request)
	return redirect('/')


