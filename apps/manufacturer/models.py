from django.db import models
from django.contrib import admin
from link.models import Link, LinkInline
from django.forms import ModelForm
from django.contrib.contenttypes import generic

class Manufacturer(models.Model):
    name = models.CharField(default="",unique=True, max_length=256)
    slug = models.SlugField(max_length=256)
    description = models.TextField(default="",blank=True)
    links = generic.GenericRelation(Link)

    def get_absolute_url(self):
        return "/manufacturer/%s/" % self.slug

    def __unicode__(self):
        return self.name

    def links_formset(self):
        LinkFormset = generic.generic_inlineformset_factory(Link, extra=1)
        return LinkFormset(instance=self)

class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer

class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [LinkInline,]
admin.site.register(Manufacturer, ManufacturerAdmin)
