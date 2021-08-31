from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=150)
    about=models.TextField()
    Year=models.IntegerField()
    image=models.ImageField(upload_to='pic')

    def __str__(self):
        return self.name