from django.contrib import messages
from itertools import count, product
from django.shortcuts import render
from django.views import View
from . models import Customer, Product

from django.db.models import Count
from .forms import CustomerRegistrationForm, ProfileForm
# Create your views here.
def home(request):
    return render(request, 'ecoapp/home.html')
    
def about(request):
    return render(request, 'ecoapp/about.html')
def contact(request):
    return render(request, 'ecoapp/contact.html')



class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(Category=val)
        titles_with_count = Product.objects.filter(Category=val).values('title').annotate(total=Count('title'))
        return render(request, 'ecoapp/category.html', {'products': products, 'titles_with_count': titles_with_count})
    
class ProductDetail(View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'ecoapp/product.html', {'product': product})
class ProfileView(View):
    def get(self , request):
        form = ProfileForm
        return render(request, 'ecoapp/profile.html', {'form': form})
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
def adress(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'ecoapp/adress.html', {'add': add})
class UpdateView(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = ProfileForm(instance=add)  # Pass the instance to the form for updating
        return render(request, 'ecoapp/updateadd.html', {'add': add, 'form': form})

    def post(self, request, pk):
        add = Customer.objects.get(pk=pk)  # Fetch the customer object
        form = ProfileForm(request.POST, instance=add)  # Pass the instance to the form
        if form.is_valid():
            form.save() 
            return render(request, 'ecoapp/updateadd.html', {'add': add, 'form': form})  
        else:
            
            return render(request, 'ecoapp/updateadd.html', {'add': add, 'form': form})
    