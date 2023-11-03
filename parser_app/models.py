from django.db import models

class LalafoProducts(models.Model):
    title_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    title_url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return (f'{self.title_name} - {self.title_url}')
