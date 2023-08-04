
from django.db import models


class Catagory(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)
    image = models.CharField(max_length=300, null=True, blank=True )
    description = models.CharField(max_length=500, null=True,blank=True, verbose_name='Description')

    class Meta:
        verbose_name_plural = 'Catagory'

    def __str__(self):
        return str(self.name) 
    
class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Tag"
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='blog/images', null=True, blank=True)
    catagories = models.ForeignKey(Catagory,on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')  
    
    
