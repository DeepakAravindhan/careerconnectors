from django.shortcuts import render, redirect
from django.contrib import messages
from c2c.models import NewUser  # Ensure you import your model
from django.http import HttpResponse


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Corrected syntax
        email = request.POST.get('email')  # Corrected syntax
        password = request.POST.get('password')  # Corrected syntax

        # Check if the email already exists
        if NewUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')

        # Create a new user instance
        new_user = NewUser(name=name, email=email, password=password)
        new_user.save()  # Save the instance to the database

        messages.success(request, 'Account created successfully!')
        return redirect('home')  # Redirect to home or another page

    return render(request, 'signup.html')  # Render the signup form

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user exists in the database
        try:
            user = NewUser.objects.get(email=email, password=password)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to home page after successful login
        except NewUser.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')  # Redirect back to login page if login fails

    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def job(request):
    return render(request, 'job.html')

def syllabus(request):
    return render(request, 'syllabus.html')

def enquiry(request):
    return render(request, 'enquiry.html')

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request,'about.html')

def soft(request):
    return render(request,'soft.html')

def dm(request):
    return render(request,'dm.html')

def f_m(request):
    return render(request, 'f_m.html')

def softdev(request):
    return render(request, 'softdev.html')