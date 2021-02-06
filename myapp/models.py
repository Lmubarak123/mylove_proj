from django.db import models
from django.db import models

# Create your models here.
class Lovers(models.Model):
    firstlv1=models.CharField(max_length=20)
    secondlv1=models.CharField(max_length=20)
    sweet=models.CharField(max_length=30)
    favcolor=models.CharField(max_length=30)
    oneword=models.CharField(max_length=30)

