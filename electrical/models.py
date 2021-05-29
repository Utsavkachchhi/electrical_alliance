from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib import admin

from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):
    is_distributors = models.BooleanField(default=False)
    is_dealers = models.BooleanField(default=False)


class Dealers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=15, blank=False)
    l_name = models.CharField(max_length=15, blank=False)
    city = models.CharField(max_length=15, blank=False)
    phone_num = models.IntegerField(default='')
    address = models.TextField(default='', blank=False)

    def __str__(self):
        return self.user.username


class Distributors(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dname = models.CharField(max_length=15, blank=False)
    info = models.CharField(max_length=20,blank=False)
    min_ord = models.CharField(max_length=5,blank=False)
    location = models.CharField(max_length=40,blank=False)
    d_logo = models.FileField(blank=False, default='')

    Dis_Status_Available = "Available"
    Dis_Status_NotAvailable = "NotAvailable"
    Dis_choice = ((Dis_Status_Available, Dis_Status_Available),
                  (Dis_Status_NotAvailable, Dis_Status_NotAvailable)
                  )
    status = models.CharField(max_length=50, choices=Dis_choice, default=Dis_Status_Available, blank=False)
    approved = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.dname


class Item(models.Model):
    image = models.ImageField(upload_to='ele/images',default='')
    id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=30, blank=False)
    category = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.pname


class Menu(models.Model):
    image = models.ImageField(upload_to='ele/images', default='')
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    d_id = models.ForeignKey(Distributors, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.item_id.pname + ' - ' + str(self.price)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total_amount = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    delivery_addr = models.CharField(max_length=50, blank=True)
    orderedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    d_id = models.ForeignKey(Distributors, on_delete=models.CASCADE)

    ORDER_STATE_WAITING = "Waiting"
    ORDER_STATE_PLACED = "Placed"
    ORDER_STATE_ACKNOWLEDGED = "Acknowledged"
    ORDER_STATE_COMPLETED = "Completed"
    ORDER_STATE_CANCELLED = "Cancelled"
    ORDER_STATE_DISPATCHED = "Dispatched"

    ORDER_STATE_CHOICES = (
        (ORDER_STATE_WAITING, ORDER_STATE_WAITING),
        (ORDER_STATE_PLACED, ORDER_STATE_PLACED),
        (ORDER_STATE_ACKNOWLEDGED, ORDER_STATE_ACKNOWLEDGED),
        (ORDER_STATE_COMPLETED, ORDER_STATE_COMPLETED),
        (ORDER_STATE_CANCELLED, ORDER_STATE_CANCELLED),
        (ORDER_STATE_DISPATCHED, ORDER_STATE_DISPATCHED)
    )
    status = models.CharField(max_length=50, choices=ORDER_STATE_CHOICES, default=ORDER_STATE_WAITING)

    def __str__(self):
        return str(self
                   .id) + ' ' + self.status


class orderItem(models.Model):
        id = models.AutoField(primary_key=True)
        item_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
        ord_id = models.ForeignKey(Order, on_delete=models.CASCADE)
        quantity = models.IntegerField(default=0)

        def __str__(self):
            return str(self.id)


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    product = models.ForeignKey(Item,on_delete=models.SET_NULL,null=True)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.customer_name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

