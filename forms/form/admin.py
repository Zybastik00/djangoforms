from django.contrib import admin

from .models import Animals,Char

class AnimalsAdmin(admin.ModelAdmin):
    list_display =('name','type1')
    search_fields =('name','type1')

class CharAdmin(admin.ModelAdmin):
    list_display = ('color','age')
    search_fields = ('color','age')

admin.site.register(Animals,AnimalsAdmin)
admin.site.register(Char,CharAdmin)