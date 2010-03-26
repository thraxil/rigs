from models import Manufacturer, Link
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes import generic

def edit_links(request,object_id):
    manufacturer = get_object_or_404(Manufacturer,id=object_id)
    LinksFormset = generic.generic_inlineformset_factory(Link, extra=1)
    if request.method == 'POST':
        formset = LinksFormset(request.POST, request.FILES,instance=manufacturer)
        if formset.is_valid():
            formset.save()
    return HttpResponseRedirect(manufacturer.get_absolute_url())
