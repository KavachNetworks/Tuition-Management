from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request,"home.html")

def contact_us(request):
    return render(request,"contactus.html")

def signin(request):
    return render(request,"registrations/signin.html")

def signup(request):
    return render(request,"registrations/signup.html")        

