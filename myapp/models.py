from django.db import models

# Create your models here.
class Item(models.Model):
    name= models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Bill(models.Model):
    items = models.ManyToManyField(Item, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Bill {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    
    @property 
    def total_price(self):
        return sum(item.price for item in self.items.all())