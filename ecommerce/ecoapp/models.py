from django.db import models
from django.contrib.auth.models import User




# Create your models here.
CATEGORY_CHOICES=(
   ('CR', 'Curd'),
   ('ML', 'Milk'),
   ('GH', 'Ghee'),
   ('MS', 'Milk Shake'),


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

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrected on_delete
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    county = models.CharField(max_length=60)
    mobile = models.CharField(max_length=50, )  # Corrected spelling and added length
    city = models.CharField(choices=STATE_CHOICES, max_length=100)  # Corrected variable name to STATE_CHOICES
    def __str__(self):
        return self.name


    
