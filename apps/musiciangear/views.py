from models import MusicianGear, Link, Photo
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic

def edit_links(request,id):
    musiciangear = get_object_or_404(MusicianGear,id=id)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES,instance=musiciangear)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musiciangear.get_absolute_url())

def edit_photos(request,id):
    musiciangear = get_object_or_404(MusicianGear,id=id)
    PhotosFormset = generic.generic_inlineformset_factory(Photo, extra=1)
    if request.method == 'POST':
        formset = PhotosFormset(request.POST, request.FILES,instance=musiciangear)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musiciangear.get_absolute_url())
