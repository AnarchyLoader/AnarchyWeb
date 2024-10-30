from django.db import models


class Hack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    process = models.CharField(max_length=100, default='hl.exe')
    source = models.CharField(max_length=300, default='https://google.com')
    game = models.CharField(max_length=100, default='CS 1.6')
    
    def __str__(self):
        return self.name