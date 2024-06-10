from django.db import models
from django.contrib.auth.models import User




# Create your models here.
CATEGORY_CHOICES=(
   ('CR', 'Curd'),
   ('ML', 'Milk'),
   ('GH', 'Ghee'),
   ('MS', 'Milk Shake'),
   ('BT', 'Belts'),
   ('WT', 'Watches'),


)



class  Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price= models.FloatField()
    discount_price = models.TextField()

    description= models.TextField()
    composition = models.TextField(default='')
    Category = models.CharField( choices = CATEGORY_CHOICES, max_length =2)
    product_image = models.ImageField(upload_to='product')
 
    def __str__(self):
      return self.title

STATE_CHOICES = (  # Corrected variable name to STATE_CHOICES
    ('Nakuru', 'Nakuru'),
    ('Nairobi', 'Nairobi'),
    ('Mombasa', 'Mombasa'),
    ('Kisumu', 'Kisumu'),
    ('Eldoret', 'Eldoret')
      # Added a comma at the end of each tuple
)

STATUS_CHOICES=(
    ('pedding', 'pedding'),
    ('cancel', 'canceled'),
    ('delivered','delivered'),
    ('shipped', 'Shipped')

)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrected on_delete
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    county = models.CharField(max_length=60)
    mobile = models.CharField(max_length=50, )  # Corrected spelling and added length
    city = models.CharField(choices=STATE_CHOICES, max_length=100)  # Corrected variable name to STATE_CHOICES
    def __str__(self):
        return self.name
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total(self):
        return self.quantity * (self.product.selling_price - self.product.discount_price)
""" 
class payment(models.Model):
    paid= models.BooleanField(defalult=False)
    amount =models.FloatField()
    razorpay_order_id=models.CharField(max_length=100, blank=True , null=True)
    razor_payment_status =models.CharField(max_length=100, blank=True, null=True)

class OrderPlaced(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     customer = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField(default=1)
     order_date=models.DateTimeField(auto_now_add=True)
     status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')
     
     def total_cost(self):
        return self.quantity * self.product.discounted_price


"""
    
