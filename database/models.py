# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Ability(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    ability_name = models.CharField(primary_key=True, max_length=15)
    char = models.ForeignKey('Comiccharacter')
    def __unicode__(self):
        return self.ability
    class Meta:
        managed = False
        db_table = 'ability'
        unique_together = (("ability_name", "char"),)

class Alias(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    char = models.ForeignKey('Comiccharacter')
    alias_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.alias_name
    class Meta:
        managed = False
        db_table = 'alias'
        unique_together = (("char", "alias_name"),)

class Charactertocomic(models.Model):
    char = models.ForeignKey('Comiccharacter')
    comic = models.ForeignKey('Comic')
    def __unicode__(self):
        return (self.char + " " + self.comic)
    class Meta:
        managed = False
        db_table = 'charactertocomic'
        unique_together = (("char", "comic"),)

class Comic(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    title = models.CharField(max_length=200)
    issue_num = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.CharField(max_length=50)
    series_title = models.CharField(max_length=200)
    series_id = models.CharField(max_length=15)
    release_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __unicode__(self):
        return self.title
    class Meta:
        managed = False
        db_table = 'comic'

class Comiccharacter(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    real_name = models.CharField(max_length=100)
    current_alias = models.CharField(max_length=100)
    def __unicode__(self):
        return self.real_name
    class Meta:
        managed = False
        db_table = 'comiccharacter'

class Comictocreator(models.Model):
    comic = models.ForeignKey('Comic')
    creator = models.ForeignKey('Creator')
    def __unicode__(self):
        return (self.comic + " " + self.creator)
    class Meta:
        managed = False
        db_table = 'comictocreator'
        unique_together = (("comic", "creator"),)

class Creator(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'creator'

class Event(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=800)
    previous_event = models.CharField(max_length=15, blank=True)
    next_event = models.CharField(max_length=15, blank=True)
    def __unicode__(self):
        return self.title
    class Meta:
        managed = False
        db_table = 'event'

