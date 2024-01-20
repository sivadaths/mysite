from django.db import models

# Create your models here.

class TOdo(models.Model):
    todo = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    
