from django.conf.urls.defaults import *

from musician.models import Musician, MusicianForm
from tagging.views import tagged_object_list

info_dict = {
    'queryset': Musician.objects.all(),
}

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
                       (r'^create/?$', 'django.views.generic.create_update.create_object',
                        dict(form_class=MusicianForm, post_save_redirect="/musician/") ),
                       (r'^(?P<slug>[^/]+)/update/?$', 'django.views.generic.create_update.update_object',
                        dict(form_class=MusicianForm, post_save_redirect="/musician/") ),
                       (r'^(?P<slug>[^/]+)/delete/?$', 'django.views.generic.create_update.delete_object',
                        dict(model=Musician, post_delete_redirect="/musician/") ),
                       url(r'^tag/(?P<tag>[^/]+)/$',tagged_object_list,dict(queryset_or_model=Musician, paginate_by=100, allow_empty=True,
                                                                            template_name="musician/musician_tag_list.html"),
                           name='musician_tag_detail'),
                       (r'^(?P<slug>[^/]+)/edit_links/?$', 'musician.views.edit_links'),
                       (r'^(?P<slug>[^/]+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)
