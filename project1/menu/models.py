from django.db import models

class Catagory(models.Model):  # spelling same as your HTML file
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Catagories"

    def __str__(self):
        return self.name

class Product(models.Model):
    catagory = models.ForeignKey(Catagory, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name
