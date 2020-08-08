from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
# Create your models here.

class Note(models.Model):
    user  = models.ForeignKey(User , on_delete  = models.CASCADE)
    title = models.CharField(max_length=50)
    slug  = models.SlugField(null = True , blank = True )
    content = models.TextField(blank = True)
    active = models.BooleanField(default = True)
    created = models.DateTimeField(blank = True ,default = datetime.datetime.now)
    tags = models.CharField(max_length=50 , blank = True)
    img = models.ImageField(upload_to = "notes-img")

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify (self.title)
            super(Note , self).save(*args , **kwargs)



    def __str__(self):
        return self.title
