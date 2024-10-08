from django.db import models
from django.conf import settings
# Create your models here.

class record(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False) 
    create_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.CharField(max_length=20,unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name + "   " + self.last_name


