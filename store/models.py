from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    
    
class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    


class Product(models.Model):
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='product')
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title
    

