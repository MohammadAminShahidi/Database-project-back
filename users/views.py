from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def home(request):
	return render (request=request, template_name="users/base.html", context={})

def staff_dashboard(request):
	return render (request=request, template_name="users/staff-dashboard.html", context={})

def citizen_dashboard(request):
	return render (request=request, template_name="users/citizen-dashboard.html", context={})
	
def register(request):
	if request.method == "POST":
		user_form = NewUserForm(request.POST)
		staff_form = Staff_NIDForm(request.POST)

		if user_form.is_valid() and staff_form.is_valid():
			user = user_form.save()
			staff = staff_form.save(commit=False)
			staff.user = user
			staff.save()
			messages.success(request, "Registration successful." )
			return redirect("users:login")

		messages.error(request, "Unsuccessful registration. Invalid information.")

	else:
		user_form = NewUserForm()
		staff_form = Staff_NIDForm()
		

	return render (request=request, template_name="users/signup.html", context={"user_form":user_form, "staff_form" : staff_form})

def citizen_register(request):
	if request.method == "POST":
		user_form = NewUserForm(request.POST)
		citizen_form = Citizen_Form(request.POST)

		if user_form.is_valid() and citizen_form.is_valid():
			user = user_form.save()
			citizen = citizen_form.save(commit=False)
			citizen.user = user
			citizen.save()
			messages.success(request, "Registration successful." )
			return redirect("users:citizen-login")

		messages.error(request, "Unsuccessful registration. Invalid information.")

	else:
		user_form = NewUserForm()
		citizen_form = Citizen_Form()
		

	return render (request=request, template_name="users/citizen-signup.html", context={"user_form":user_form, "citizen_form" : citizen_form})
	
def staff_login(request):

	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("users:staff-dashboard")

			messages.error(request,"Invalid username or password.")

		else:
			messages.error(request,"Invalid username or password.")

	login_form = AuthenticationForm()
	return render(request=request, template_name="users/login.html", context={"login_form":login_form})

def citizen_login(request):

	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("users:citizen-dashboard")

			messages.error(request,"Invalid username or password.")

		else:
			messages.error(request,"Invalid username or password.")

	login_form = AuthenticationForm()
	return render(request=request, template_name="users/citizen-login.html", context={"login_form":login_form})