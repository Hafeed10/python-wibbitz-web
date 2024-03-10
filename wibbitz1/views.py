import json 
from django.shortcuts import render, get_object_or_404
from wibbitz1.models import Customer, Featured
from django.db import IntegrityError
from .models import *
from django.urls import reverse
from django.http.response import HttpResponse

# from wibbitz1.forms import ContactForm


app_name = 'wibbitz1'

def index(request):
    customers = Customer.objects.all()
    latest_customers =  Latest_customer.objects.all() [:4]
    featureds = Featured.objects.all()
    videoblogs = Videoblog.objects.all()
    videoresources = Videoresources.objects.all()
    business = Business.objects.all()
    marketings = Marketing.objects.all()
    testimonials = Testimonial.objects.all()
    contacts = Contact.objects.all()
    imgs = Img.objects.all()
    
    
    # form = ContactForm()
    
    context = {
        "name": "wibbitz1",
        "customers": customers,
        "featureds": featureds,
        "videoblogs": videoblogs,
        "videoresources": videoresources,
        "business": business,
        "marketings": marketings,
        "testimonials": testimonials,
        "contacts": contacts,
        # "form": form
        "imgs": imgs,
       "latest_customers": latest_customers,
       
    }
   
    return render(request, 'index.html', context=context)


def subscribe(request):
    email = request.POST.get('email')

    if not Subscribe.objects.filter(email=email).exists():
        Subscribe.objects.create(email=email)
        response_data = {
            "status": "success",
            "message": "Your subscription has been",
            "title": "Successfully Registered"
        }
    else:
        response_data = {
            "status": "error",
            "message": "Your subscription has already been",
            "title": "Already Registered"
        }
    
    return HttpResponse(json.dumps(response_data), content_type="application/javascript")


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        company = request.POST.get('company')
        company_size_choices = request.POST.get('company_size_choices')
        industry_choices = request.POST.get('industry_choices')
        job_role_choices = request.POST.get('job_role_choices')
        country_choices = request.POST.get('country_choices')
        user = request.POST.get('user')
        
        if not Contact.objects.filter(email=email).exists():
            Contact.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                company=company,
                company_size_choices=company_size_choices,
                industry_choices=industry_choices,
                job_role_choices=job_role_choices,
                country_choices=country_choices,
                user=user
            )
            response_data = {
                "status": "success",
                "message": "Your subscription has been successfully registered.",
                "title": "Successfully Registered"
            }
        else:
            response_data = {
                "status": "error",
                "message": "Your subscription has already been registered.",
                "title": "Already Registered"
            }

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def product(request, pk):
    business = get_object_or_404(Business, pk=pk)
    
    customer = Customer.objects.last()
     # Fetch all logos related to the business or adjust the query as needed
     # Fetch all logos related to the business or adjust the query as needed

    context = {
        'business': business,
        'customer': customer,
    }
    return render(request, 'product.html', context)