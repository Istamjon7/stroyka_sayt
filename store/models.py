from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Category',null=True,blank=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Product')
    price = models.FloatField()
    description = models.TextField()
    color = models.ManyToManyField(Color,null=True,blank=True)