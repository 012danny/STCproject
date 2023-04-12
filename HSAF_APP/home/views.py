from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.forms import newtripform
from home.models import posts, AuthUser
from django.contrib.sessions.models import Session



#view for the users profile page to show user logs
def profile(request):
	logs = posts.objects.filter(userid = request.user.id) # filter to only show logs for the current user.
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







#view for home page where users will be welcomed or sent to their profile page if logged in "index.html"
def landingpage(request):
    return render(request,'landingpage.html',{})







#view for the add new trip page. Allows users to insert a new trip. 
def newtrip(request):
	
	if request.method == 'POST' :
			
		form = newtripform(request.POST)                              # pulling from forms.py what we want to be shown as a form
				
		if form.is_valid():
			title = form.cleaned_data.get('title')                    # storing what the user entered into the text box 
			content = form.cleaned_data.get('content')                # storing what the user entered into the text box 
			userid = request.user.id                                  # inserting the current users id into the userid field 
			form = posts(title=title, content=content, userid=userid) # passing stored information into the posts model 
			form.save()                                               # POST information into the Db 
			return redirect('/profile')	                              #redirect  
			
	else:
		form = newtripform()
	return render(request,'newtrip.html',{'form': form})





#view for the stringer page
def mystringer(request):
    return render(request,'mystringer.html',{})





#uses current post id to get data from DB associated with the post id 
def edit(request, post_id):
	editpost = posts.objects.get(post_id=post_id) # gets the post id for the post to be edited and populates the fields on the HTML page

	return render(request,'edit.html',{'editpost': editpost})  




# update the information from the selected post. continuation of "def edit" when save edit btn clicked activates this function
def update(request, post_id):

	editpost = posts.objects.get(post_id=post_id)     #gets the post id for the post to be updated with the changes
	form = newtripform(request.POST, instance = editpost) # will update the information with the new inputs by the user
	if form.is_valid():
		form.save()                                      # posting the changes
		return redirect('/')                             # redirecting after changes have been saved back to porfile 

	return render(request,'edit.html', {'editpost': editpost})




# to delete a post from the user


def delete(request, post_id):

	deletepost = posts.objects.get(post_id=post_id)  # gets the post id for the selected post to be deleted.
	deletepost.delete()
	return redirect('/')







#sign In view to log the user in and to the profile page
def signin(request):
	if request.user.is_authenticated:
		return render(request, 'landingpage.html')
	if request.method == 'POST':
		username = request.POST['username']     								#grabbing the username and password from user 
		password = request.POST['password']
		user = authenticate(request, username=username, password=password) 		#authenticating user with django lib
		if user is not None:
			login(request, user)
			return redirect('/profile')  										# if successful authentication send user to profile page.
		else:
			msg = 'Login Error'  		 										#if error in authentication let them try agian and display login error.
			form = AuthenticationForm(request.POST)
			return render(request, 'login.html', {'form' : form, 'msg': msg})	
	else:
		form = AuthenticationForm()
		return render(request, 'login.html', {'form': form})










#Logout view to log the user out and back to home page
def signout(request):
	logout(request)
	return redirect('/')


