from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title