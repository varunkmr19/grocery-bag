from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey

# Create your models here.


class User(AbstractUser):
    pass


class Item(models.Model):
    ITEM_STATUS = (
        ('PENDING', 'PENDING'),
        ('BOUGHT', 'BOUGHT'),
        ('NOT_AVAILABLE', 'NOT AVAILABLE')
    )
    name = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    status = models.CharField(
        max_length=15, choices=ITEM_STATUS, default='PENDING')
    date = models.DateField()

    def __str__(self):
        return self.name


class GroceryList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='list')
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='item_list')

    def __str__(self):
        return self.user.username
