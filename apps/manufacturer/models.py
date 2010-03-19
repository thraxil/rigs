from django.db import models
from django.contrib import admin

class Manufacturer(models.Model):
    name = models.CharField(default="",unique=True, max_length=256)
    slug = models.SlugField(max_length=256)
    description = models.TextField(default="",blank=True)

    def get_absolute_url(self):
        return "/manufacturer/%d/" % self.id

class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
