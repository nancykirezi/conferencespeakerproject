from django.db import models

# Create your models here.
class Speaker(models.Model):
    id = models.int(max_length=6)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact_info = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='speakers/')
    areas_of_expertise = models.TextField()

    def __str__(self):
        return self.name
