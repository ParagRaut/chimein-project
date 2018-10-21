from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Product

# Create your views here.

def home_page(request):
    context = {}
    return render(request, 'products/home_page.html', context)

@login_required
def products_create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            print("1")
            errorcontext = {'error':'All fields are mandatory'}
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.chimer = request.user
            product.save()
            return redirect('home-page')

    else:
        context = {}
        return render(request, 'products/product_create_page.html', context)
