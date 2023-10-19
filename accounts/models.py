from django.db import models

# Create your models here.
class transactions(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    debit = models.IntegerField()
    credit = models.IntegerField()
    acbal = models.IntegerField()

    def __str__(self):
        return self.name

class customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    avail_bal = models.IntegerField()

    def __str__(self):
        return self.name
