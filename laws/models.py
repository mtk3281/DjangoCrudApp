<<<<<<< HEAD
from typing import Any
=======
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
from django.db import models
from django.conf import settings
# Create your models here.

class law_data(models.Model):
    year = models.IntegerField(null=True,default=2024,blank=True)
    number = models.IntegerField(null=False,default=0,blank=False)

    def __str__(self):
        return " year & no" +str(self.year) + " " + str(self.number)

<<<<<<< HEAD
=======

>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
