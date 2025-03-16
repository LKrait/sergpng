from django.db import models
import random

def GenID():
    return str(random.randrange(1000,9999,1))+str(random.randrange(1000,9999,1))


class Post(models.Model):
    postid = models.CharField(max_length=10, primary_key=True, default=GenID, editable=False)
    author = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(max_length=1048)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.content}, {self.author}. [Posted: {self.posted}]'