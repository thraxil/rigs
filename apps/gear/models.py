from django.db import models
from django.contrib import admin
from manufacturer.models import Manufacturer
import tagging
import tagging.fields

class Gear(models.Model):
    name = models.CharField(default="",max_length=256)
    slug = models.SlugField(max_length=256)
    manufacturer = models.ForeignKey(Manufacturer)
    description = models.TextField(default="",blank=True)
    tags = tagging.fields.TagField()

    def get_absolute_url(self):
        return "/gear/%d/" % self.id

    def __unicode__(self):
        return self.name
#tagging.register(Gear)

class GearAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
