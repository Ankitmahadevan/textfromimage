from django.db import models

from django.urls import reverse
class Car(models.Model):
    #name = models.CharField(max_length=255)
    #price = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='carsf/',blank=True)
#     def __str__(self):
#     	return self.name
    def get_absolute_url(self):
    	return reverse('postsdetail', args=[str(self.id)])    