from django.db import models

quality = (('HIGH','high'),('LOW','low'),('MEDIUM','medium'))
size = ((10,'TEN'),(20,'TWENTY'),(30,'THIRTY'))
colour = (('RED','red'),('BLUE','blue'),('GREEN','green'),('BLACK','black'))


class ProductMainModel(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=700)
    Price = models.DecimalField(max_digits=9,decimal_places=2)
    Size = models.CharField(max_length=50, choices = size)
    Quality = models.CharField(max_length=50, choices = quality)

class productColourModel(models.Model):
    table1 = models.ForeignKey(ProductMainModel,on_delete=models.CASCADE)
    Product = models.CharField(max_length=500)
    Colour = models.CharField(max_length=50, choices = colour)

class productImageModel(models.Model):
    table1 = models.ManyToManyField(ProductMainModel)
    table2 = models.ManyToManyField(productColourModel)
    Product = models.CharField(max_length=500)
    Image = models.ImageField()

    
