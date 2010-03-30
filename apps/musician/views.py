from models import Musician, Link
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic

def edit_links(request,slug):
    musician = get_object_or_404(Musician,slug=slug)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES,instance=musician)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(musician.get_absolute_url())
