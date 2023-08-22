from django.db import models
from django.core.validators import MaxValueValidator

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonial/images', null=True, blank=True,)
    star_rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name