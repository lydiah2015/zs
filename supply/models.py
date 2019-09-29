from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=45)
    
    def __str__(self):
        return self.Name

    def save_image(self):
        return self.save()

    class Meta:
        ordering = ['image']
