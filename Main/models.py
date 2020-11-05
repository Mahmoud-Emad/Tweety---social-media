from django.db import models

# Create your models here.



class image(models.Model):
    image = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="Top Image")
    name = models.CharField(max_length=100,null=True ,blank=True,verbose_name="Top Image")
    
    
    def __str__(self):
        return self.name