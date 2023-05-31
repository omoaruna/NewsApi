from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
     ordering = ["-date_posted"]#to reverse order of posts
     verbose_name_plural = "News"

# Create your models here.
