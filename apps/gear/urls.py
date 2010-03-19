from django.conf.urls.defaults import *

from gear.models import Gear

info_dict = {
    'queryset': Gear.objects.all(),
}

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
                       (r'^create/?$', 'django.views.generic.create_update.create_object',
                        dict(model=Gear, post_save_redirect="/gear/") ),
                       (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)

