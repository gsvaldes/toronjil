from django.db import models

class Entry(model.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
        return self.title
        
        
    class Meta(object):
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ['-created']
