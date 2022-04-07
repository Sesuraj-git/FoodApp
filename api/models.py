from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=20, blank=False)
    l_name = models.CharField(max_length=20, blank=False)
    college_id = models.CharField(max_length=6, default=0)
    college_mail = models.EmailField(max_length=256)
    phone = models.CharField(max_length=10, blank=False)
    address = models.TextField()

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rname = models.CharField(max_length=100, blank=False)
    info = models.CharField(max_length=40, blank=False)
    min_ord = models.CharField(max_length=5, blank=False)
    location = models.CharField(max_length=40, blank=False)
    r_logo = models.FileField(blank=False)

    REST_STATE_OPEN = "Open"
    REST_STATE_CLOSE = "Closed"
    REST_STATE_CHOICES = (
        (REST_STATE_OPEN, REST_STATE_OPEN),
        (REST_STATE_CLOSE, REST_STATE_CLOSE)
    )
    status = models.CharField(max_length=50, choices=REST_STATE_CHOICES, default=REST_STATE_OPEN, blank=False)
    is_approved = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.rname


class Timings(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    opening_time = models.TimeField(auto_now=False)
    closing_time = models.TimeField(auto_now=False)



class Menu(models.Model):
    item_name = models.CharField(max_length=30, blank=False)
    r_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.item_name + ' - ' + str(self.price)


class Order(models.Model):
    total_amount = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    delivery_in = models.CharField(max_length=50, blank=True)
    orderedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    r_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

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
        return str(self.id) + ' ' + self.status


class Cart(models.Model):
    item_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    ord_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def cart_total(self):
        total = self.item_id.price*self.quantity
        print(total)
        return total
    def __str__(self):
        return str(self.id)
