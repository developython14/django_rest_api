from django.contrib import admin
from .models import Person ,Cours ,Snippet
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name' , )
    search_fields = ['first_name' ,  'last_name']
    list_filter  =  ['first_name' ]
    filter_horizontal = ('Cours',)


admin.site.register(Person ,AuthorAdmin )

admin.site.register(Cours )
admin.site.register(Snippet )