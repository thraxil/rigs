from django.conf.urls.defaults import *

from manufacturer.models import Manufacturer

info_dict = {
    'queryset': Manufacturer.objects.all(),
}

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
                       (r'^create/?$', 'django.views.generic.create_update.create_object',
                        dict(model=Manufacturer, post_save_redirect="/manufacturer/") ),
                       (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)
