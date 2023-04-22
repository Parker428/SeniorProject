from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import CompanyReview, CompanyContact


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']
        s = CompanyContact(fname=fname, lname=lname, email=email, message=message)
        s.save()

    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def reviews(request):
    if request.method == "POST":
        name= request.POST["name"]
        message = request.POST['message']
        s = CompanyReview(message=message, name=name)
        s.save()
        return redirect('reviews')
        
    return render(request, 'reviews.html')

def reviewlist(request):
    reviews = CompanyReview.objects.all()
    return render(request, 'reviewlist.html', {'message': reviews})

def services(request):
    return render(request, 'services.html')