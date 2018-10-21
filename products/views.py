from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Product

# Create your views here.

def home_page(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products/home_page.html', context)

@login_required
def products_create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
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
            return redirect('/products/' + str(product.id))

    else:
        context = {}
        return render(request, 'products/product_create_page.html', context)

def products_detail(request, product_id):
    product =  get_object_or_404(Product, pk=product_id)
    context = {'product':product}
    return render(request, 'products/product_detail_page.html', context)

@login_required(login_url="/accounts/signup")
def products_upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
