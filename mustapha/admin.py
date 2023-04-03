from django.contrib import admin
from .models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name' , )
    search_fields = ['first_name' ,  'last_name']
    list_filter  =  ['first_name' ]
    filter_horizontal = ('Cours',)


class fillierAdmin(admin.TabularInline):
    model = fillier


class niveauAdmin(admin.ModelAdmin):
    inlines = [
        fillierAdmin,
    ]


class module_fillier(admin.StackedInline):
    model = matier

class fillier_m_admin(admin.ModelAdmin):
    inlines = [
        module_fillier,
    ]


class chapitre_ad(admin.ModelAdmin):
    list_display = ('title' ,)



admin.site.register(Niveau , niveauAdmin )
admin.site.register(fillier , fillier_m_admin )
admin.site.register(matier  )
admin.site.register(cour  )
admin.site.register(chapitre ,chapitre_ad )

