from django.db import models

class ProductMainModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    unique_code = models.CharField(max_length=100, unique=True)
    SIZE_CHOICES = [
        (10, 10),
        (20, 20),
        (30, 30),
    ]
    size = models.IntegerField(choices=SIZE_CHOICES)
    QUALITY_CHOICES = [
        ('high', 'High'),
        ('low', 'Low'),
        ('medium', 'Medium'),
    ]
    quality = models.CharField(max_length=10, choices=QUALITY_CHOICES)

class ProductColourModel(models.Model):
    product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)
    COLOUR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    colour = models.CharField(max_length=10, choices=COLOUR_CHOICES)

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
