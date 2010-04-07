from models import Manufacturer, Link
from gear.models import AddGearForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic

def edit_links(request,slug):
    manufacturer = get_object_or_404(Manufacturer,slug=slug)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES,instance=manufacturer)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(manufacturer.get_absolute_url())


def add_gear(request,slug):
    manufacturer = get_object_or_404(Manufacturer,slug=slug)
    if request.method == 'POST':
        form = AddGearForm(request.POST, request.FILES)
        if form.is_valid():
            newgear = form.save(commit=False)
            newgear.manufacturer = manufacturer
            newgear.save()
            form.save_m2m()
            return HttpResponseRedirect(newgear.get_absolute_url())
        else:
            print "not valid!"
            print form.errors
    return HttpResponseRedirect(manufacturer.get_absolute_url())
