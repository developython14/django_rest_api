from django.contrib import admin
from .models import Person
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ['first_name' ,  'last_name']


admin.site.register(Person ,AuthorAdmin )