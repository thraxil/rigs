from models import Musician, Link, Photo
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic
from django.forms.models import inlineformset_factory

def edit_links(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES,instance=musician)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musician.get_absolute_url())

def edit_photos(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    PhotosFormset = generic.generic_inlineformset_factory(Photo, extra=1)
    if request.method == 'POST':
        formset = PhotosFormset(request.POST, request.FILES,instance=musician)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musician.get_absolute_url())


def edit_gear(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    from musiciangear.models import MusicianGear
    GearFormSet = inlineformset_factory(Musician, MusicianGear,extra=1)
    if request.method == 'POST':
        formset = GearFormSet(request.POST, request.FILES,instance=musician)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musician.get_absolute_url())
