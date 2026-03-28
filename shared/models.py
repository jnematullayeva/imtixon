from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

class Services(BaseModel):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        db_table = 'services'
        ordering = ['-id']