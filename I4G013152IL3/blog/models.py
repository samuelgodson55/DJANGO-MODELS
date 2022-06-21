from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Model

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.Title