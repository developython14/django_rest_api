from django.contrib import admin
from .models import *
# Register your models here.
from django.urls import reverse



class fillierAdmin(admin.TabularInline):
    model = fillier
    list_display_links = ('title','niveau')


class niveauAdmin(admin.ModelAdmin):
    inlines = [
        fillierAdmin,
    ]




class cour_chapire(admin.TabularInline):
    model=cour


class chapitre_ad(admin.ModelAdmin):
    list_display_links = ('title',)
    inlines = [
        cour_chapire,
    ]





admin.site.register(Niveau  )

admin.site.register(cour )
admin.site.register(chapitre  )

