from django.db import models
from django.contrib import admin
from link.models import Link, LinkInline
from gear.models import Gear
from musician.models import Musician
from photo.models import Photo, PhotoInline
from django.contrib.contenttypes import generic

class MusicianGear(models.Model):
    musician = models.ForeignKey(Musician)
    gear = models.ForeignKey(Gear)
    description = models.TextField(default="",blank=True)
    links = generic.GenericRelation(Link)
    photos = generic.GenericRelation(Photo)
    added = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)

    def get_absolute_url(self):
        return "/musiciangear/%d/" % self.id

    def __unicode__(self):
        return "%s - %s" % (self.musician.name,self.gear.name)

    def links_formset(self):
        LinkFormset = generic.generic_inlineformset_factory(Link, extra=1)
        return LinkFormset(instance=self)

    def photos_formset(self):
        PhotoFormset = generic.generic_inlineformset_factory(Photo, extra=1)
        return PhotoFormset(instance=self)

    def first_photo(self):
        if self.photos.count() > 0:
            return self.photos.all()[0]
        else:
            return None
    def type_display(self):
        return "Musician Gear"


class MusicianGearAdmin(admin.ModelAdmin):
    inlines = [LinkInline,PhotoInline]
admin.site.register(MusicianGear, MusicianGearAdmin)
