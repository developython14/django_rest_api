from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django import forms
from django.forms.widgets import TextInput

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Niveau(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    abrev = models.CharField(max_length=100, blank=True, default='')

    def __str__(self) -> str:
        return self.title
    

class fillier(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class matier(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    fillier = models.ForeignKey(fillier, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class chapitre(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    fillier = models.ForeignKey(fillier, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title


    class Meta:
        ordering = ['created']


