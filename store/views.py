from django.shortcuts import render
from .models import Product
from django.utils.timezone import now

def home(request):

    products = Product.objects.filter(
        expiry_date__gte=now().date()
    )

    return render(request, 'home.html', {
        'products': products
    })