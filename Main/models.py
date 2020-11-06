from django.db import models
from django.contrib.auth.models import User
# from django.utils.text import slugify
# Create your models here.



class Tweet(models.Model):
    Name = models.ForeignKey(User,related_name='Tweet_Name',on_delete=models.CASCADE,verbose_name="User Name")
    Post = models.TextField(max_length=400,verbose_name="Post")
    Image = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="Post Image")
    DateTime = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(blank=True,null=True,max_length=1000)

    # def save(self,*args, **kwargs):

    #     self.slug = slugify(str(self.name) +  str(self.Post))
    #     super(Tweet,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.Name) + str(self.DateTime)