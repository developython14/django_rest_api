from django.db import models

# Create your models here.


class story(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    page_de_garde = models.ImageField(null=True,upload_to='image_stories', default='')

    class Meta:
        ordering = ['order']




class story_image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image_stories', default='')
    story = models.ForeignKey(story , related_name='snippets',on_delete=models.CASCADE, null=True, blank=True)





class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
