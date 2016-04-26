from django.contrib import admin
from database.models import Comic
from database.models import Comiccharacter
from database.models import Alias
from database.models import Creator
from database.models import Event

class ComicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'issue_num', 'series_title')
    #list_filter = ['title']
    search_fields = ['title', 'series_title']

class ComiccharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'real_name', 'current_alias')
    #list_filter = ['real_name']
    search_fields = ['real_name', 'current_alias']

class AliasAdmin(admin.ModelAdmin):
    list_display = ('alias_name', 'char')
    search_fields = ['alias_name', 'char']
    #list_filter = ['alias_name']

class CreatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    #list_filter = ['name']

class EventAdmin(admin.ModelAdmin):
    list_diplay = ('id', 'title', 'description')
    search_fields = ['title']
    #list_filter = ['title']


admin.site.register(Comic, ComicAdmin)
admin.site.register(Comiccharacter, ComiccharacterAdmin)
admin.site.register(Alias, AliasAdmin)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(Event, EventAdmin)
# Register your models here.
