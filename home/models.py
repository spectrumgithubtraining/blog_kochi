from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100, default="")
    title= models.CharField(max_length=100, default="")
    short_description= models.CharField(max_length=200, default="")
    content= models.TextField()
    thumbnail=models.ImageField(upload_to="blog_images")
    created_at = models.TimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
