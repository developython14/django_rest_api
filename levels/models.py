from django.db import models

# Create your models here.




class levels(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100,unique=True )
    abre = models.CharField(max_length=5, blank=True, default='')

    def __str__(self) -> str:
        return self.title


    class Meta:
        ordering = ['order']




class Filieres(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100,unique=True )
    abre = models.CharField(max_length=5, blank=True, default='')
    level = models.ForeignKey(levels , blank=True , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title +'ha'+ str(self.level.id)

    class Meta:
        ordering = ['order']