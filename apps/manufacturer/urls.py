from django.conf.urls.defaults import *

from manufacturer.models import Manufacturer, ManufacturerForm

info_dict = {
    'queryset': Manufacturer.objects.all(),
}

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
                       (r'^create/?$', 'django.views.generic.create_update.create_object',
                        dict(form_class=ManufacturerForm, post_save_redirect="/manufacturer/") ),
                       (r'^(?P<object_id>\d+)/update/?$', 'django.views.generic.create_update.update_object',
                        dict(form_class=ManufacturerForm, post_save_redirect="/manufacturer/") ),
                       (r'^(?P<object_id>\d+)/delete/?$', 'django.views.generic.create_update.delete_object',
                        dict(model=Manufacturer, post_delete_redirect="/manufacturer/") ),
                       (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)
