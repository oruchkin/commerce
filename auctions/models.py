from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import DecimalField, IntegerField
from django.utils import timezone

class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=40, decimal_places=10,help_text="text")
    bid = models.DecimalField(max_digits=40, decimal_places=10, help_text="text")
    category = models.CharField(max_length=500)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete= models.CASCADE)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)



class Bid(models.Model):
    pass
