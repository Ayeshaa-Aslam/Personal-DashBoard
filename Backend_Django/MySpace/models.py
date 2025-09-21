from django.db import models

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    avatar_url = models.URLField(blank=True)
    links = models.TextField(blank=True)  
    
    def __str__(self):
        return self.name

class Note(models.Model):
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:20]
