from django.db import models
from django.contrib.auth.models import *




#product detials
class productdet(models.Model):
    categorychoices=(
        ('a','eyeglass men'),
        ('b','eyeglass women'),
        ('c','eyeglass kids'),
        ('d','sunglass men'),
        ('e','sunglass women'),
        ('f','sunglass kids'),
        ('g','computer glass')
        )
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    discription=models.CharField(max_length=500)
    model=models.CharField(max_length=100)
    color=models.CharField(max_length=50)
    discount=models.IntegerField()
    quantity=models.IntegerField()
    category=models.CharField(max_length=100,default='a',choices=categorychoices)
    image=models.ImageField(upload_to='images/sunglass')
    def __str__(self) -> str:
        return f'{self.name}'
    

#cart table
class mycart(models.Model):
    products=models.ForeignKey(productdet,on_delete=models.CASCADE)
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    delivered=models.BooleanField(default=False)
    def __str__(self) -> str:
        return f'{self.usr}'
    

#wishlist table
class wish(models.Model):
    products=models.ForeignKey(productdet,on_delete=models.CASCADE)
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.usr}'
    


#messages table
class msg(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'

class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=150, null=True)
    orderstatus = (
        ('pending','pending'),
        ('Out for shipping','Out for shipping'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')

    )
    status = models.CharField(max_length=150,choices=orderstatus, default='pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def _str_(self) -> str:
        return f'{self.user},{self.tracking_no}'
    
class orderitem(models.Model):
    orderdet = models.ForeignKey(order,on_delete=models.CASCADE)
    product = models.ForeignKey(productdet,on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def _str_(self) -> str:
        return f'{self.orderdet}'


class profilee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self) -> str:
        return f'{self.user.username}'
    

class profilepic(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    propic = models.ImageField(upload_to='images/profilepic')

    def _str_(self) -> str:
        return f'{self.user.username}'