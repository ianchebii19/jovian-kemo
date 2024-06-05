from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from itertools import count, product
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
 
from django.contrib.auth import authenticate, login,logout

from . models import Customer, Product, Cart

from django.db.models import Count
from .forms import CustomerRegistrationForm, ProfileForm
# Create your views here.

@login_required
def logout_user(request):

    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'ecoapp/home.html')
    
@login_required(login_url='/accounts/login/')
def about(request):

    return render(request, 'ecoapp/about.html')



@login_required
def contact(request):
    return render(request, 'ecoapp/contact.html')





class CategoryView(View):

    @method_decorator(login_required)
    def get(self, request, val):
        products = Product.objects.filter(Category=val)
        titles_with_count = Product.objects.filter(Category=val).values('title').annotate(total=Count('title'))
        return render(request, 'ecoapp/category.html', {'products': products, 'titles_with_count': titles_with_count})
from django.utils.decorators import method_decorator
class ProductDetail(View):

    @method_decorator(login_required)
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'ecoapp/product.html', {'product': product})



from django.utils.decorators import method_decorator
class ProfileView(View):
    @method_decorator(login_required)
    def get(self , request):
        form = ProfileForm
        return render(request, 'ecoapp/profile.html', {'form': form})
    @method_decorator(login_required)
    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
          user = request.user
          name = form.cleaned_data['name']  
          location = form.cleaned_data['location']  
          county = form.cleaned_data['county'] 
          mobile = form.cleaned_data['mobile']  
          city = form.cleaned_data['city']  
          reg = Customer(user=user, name=name, county=county, location=location, city=city)
          reg.save()
          messages.success(request, 'Profile Updated  Successfully')
        else:
            messages.error(request, 'Invalid input')
        return render(request, 'ecoapp/profile.html', {'form': form})
       
     



class CustomerRegistration(View):
    
    def get(self, request):
        form = CustomerRegistrationForm()  # Instantiate your form class
        return render(request, 'ecoapp/signin.html', {'form': form})
    
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! User Registered Successfully')
        else:
            messages.error(request, 'Invalid input')
        return render(request, 'ecoapp/signin.html', {'form': form})

@login_required
def adress(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'ecoapp/adress.html', {'add': add})



class UpdateView(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = ProfileForm(instance=add)
        return render(request, 'ecoapp/updateadd.html', {'add': add, 'form': form})

    @method_decorator(login_required)
    def post(self, request, pk):
        form = ProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.location = form.cleaned_data['location']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.county = form.cleaned_data['county']
            add.save()
            messages.success(request, "Congratulations! Update Successful")
            return redirect('adress')  # Using self.success_url here
        else:
            messages.error(request, 'Invalid input')
            return render(request, 'ecoapp/updateadd.html', {'form': form})
  # Logs out the us

@login_required
def addcart(request):
     user = request.user
     product_id = request.GET.get('prod_id')  # Assuming the product ID is passed in the POST data
     product = Product.objects.get(id=product_id)
     Cart(user=user, product=product).save()
     return redirect('/showcart/')
@login_required
def showcart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = sum(p.quantity * float(p.product.discount_price) for p in cart)
    totalamount = amount + 60
    return render(request, 'ecoapp/cart.html', {'cart': cart, 'totalamount': totalamount , 'amount':   amount})



@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        # Assuming Cart model has fields: product and user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity +=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
      
        amount = 0
        for p in cart:
            value = p.quantity * float(p.product.discount_price)
            amount += value
        totalamount = amount + 60  # Assuming 60 is some fixed value
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)


@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * float(p.product.discount_price)
            amount = value
        totalamount = amount + 60  
        data = {
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
        
@login_required
def minus_cart(request):  

    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity > 1:
            c.quantity -= 1
            c.save()
        else:
            c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * float(p.product.discount_price)
            amount += value
        totalamount = amount + 60  # Assuming 60 is some fixed value
        data = {
            'quantity': c.quantity if c.quantity > 0 else 0,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)



class Checkout(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        amount = 0 
        for p in cart_items:
            value = p.quantity * float(p.product.discount_price)
            amount += value
        totalamount = amount + 60

        return render(request, 'ecoapp/checkout.html', {'add': add, 'cart_items': cart_items, 'totalamount': totalamount, 'amount': amount})