from django.contrib import admin

from .models import People

class PeopleAdmin(admin.ModelAdmin):
    list_display=('name','number_phone')
    search_fields = ('name', 'number_phone')

admin.site.register(People,PeopleAdmin)
