from django.db import models

# Create your models here.


class NewsModel(models.Model):
    header = models.CharField(max_length=200, unique=False)
    preview = models.ImageField(upload_to="uploads/news/", blank=True, null=True)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.header
    
    
class ResourceModel(models.Model):
    link = models.CharField(max_length=200)
    news = models.ForeignKey(to=NewsModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.news} | {self.link}"
    