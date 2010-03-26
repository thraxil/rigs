from models import Gear, Link, Photo
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic

def edit_links(request,slug):
    gear = get_object_or_404(Gear,slug=slug)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES,instance=gear)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(gear.get_absolute_url())

def edit_photos(request,slug):
    gear = get_object_or_404(Gear,slug=slug)
    PhotosFormset = generic.generic_inlineformset_factory(Photo, extra=1)
    if request.method == 'POST':
        formset = PhotosFormset(request.POST, request.FILES,instance=gear)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(gear.get_absolute_url())