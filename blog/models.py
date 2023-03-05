from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField 
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published")) 


class Post(models.Model): 
    title = models.CharField(max_lenght=200, unique=True)
    slug = models.SlugField(max_lenght=200, unique=True)
