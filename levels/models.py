from django.db import models

# Create your models here.




class levels(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100, blank=True, default='')
    abre = models.CharField(max_length=5, blank=True, default='')


    class Meta:
        ordering = ['order']
