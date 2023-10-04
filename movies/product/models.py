from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.URLField(max_length=200)
    #owner_key = models.ForeignKey(to=User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title