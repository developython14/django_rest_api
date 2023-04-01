from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django import forms

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']



class Cours(models.Model):
    title = models.CharField(max_length=30)
    

    def __str__(self) -> str:
        return self.title 


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Cours = models.ManyToManyField(Cours)
    

    def __str__(self) -> str:
        return self.first_name + self.last_name




class Stories(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    title = models.CharField(max_length=30 )
    last_name = models.CharField(max_length=30 ,choices=SHIRT_SIZES)
    file = forms.FileField()
    

    def __str__(self) -> str:
        return  self.title


