from django.db import models
import time


# Create your models here.
class Article(models.Model):
    SysNo = models.IntegerField(auto_created=True, primary_key=True, serialize=False)
    Title = models.CharField(max_length=50, default='Title')
    Content = models.TextField(null=True)
    Status = models.BooleanField(default=True)
    CreateUser = models.IntegerField(auto_created=True, null=False)
    CreateTime = models.DateField()
    UpdateUser = models.IntegerField(auto_created=True, null=False)
    UpdateTime = models.DateField(null=False)


    def __str__(self):
        return self.Title