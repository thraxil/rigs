from django.conf.urls.defaults import *

from gear.models import Gear
from tagging.views import tagged_object_list

info_dict = {
    'queryset': Gear.objects.all(),
}

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
                       (r'^create/?$', 'django.views.generic.create_update.create_object',
                        dict(model=Gear, post_save_redirect="/gear/") ),

                       url(r'^tag/(?P<tag>[^/]+)/$',tagged_object_list,dict(queryset_or_model=Gear, paginate_by=100, allow_empty=True,
                                                                            template_name="gear/gear_tag_list.html"),
                           name='gear_tag_detail'),
                       (r'^(?P<object_id>\d+)/update/?$', 'django.views.generic.create_update.update_object',
                        dict(model=Gear, post_save_redirect="/gear/") ),

                       (r'^(?P<object_id>\d+)/delete/?$', 'django.views.generic.create_update.delete_object',
                        dict(model=Gear, post_delete_redirect="/gear/") ),
                       (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
                       (r'^(?P<object_id>\d+)/edit_links/?$', 'gear.views.edit_links'),

)

