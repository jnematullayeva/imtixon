from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField()
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

class Services(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.price)

    class Meta:
        db_table = 'services'
        ordering = ['-id']