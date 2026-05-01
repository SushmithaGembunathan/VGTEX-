from django.shortcuts import render
from .models import Product
from django.utils.timezone import now

def home(request):
    products = Product.objects.filter(expiry_date__gte=now().date())
    return render(request, 'home.html', {'products': products})


def sarees(request):
    products = Product.objects.filter(category='saree')
    return render(request, 'sarees.html', {'products': products})


def dryfruits(request):
    products = Product.objects.filter(category='dryfruit')
    return render(request, 'dryfruits.html', {'products': products})


def healthmixes(request):
    products = Product.objects.filter(category='healthmix')
    return render(request, 'healthmixes.html', {'products': products})


def contact(request):
    return render(request, 'contact.html')


def reviews(request):
    return render(request, 'reviews.html')