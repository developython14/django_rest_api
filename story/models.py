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




