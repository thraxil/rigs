from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic.simple import direct_to_template
from django.contrib.comments.feeds import LatestCommentFeed

from django.contrib import admin
admin.autodiscover()

from account.openid_consumer import PinaxConsumer


if settings.ACCOUNT_OPEN_SIGNUP:
    signup_view = "account.views.signup"
else:
    signup_view = "signup_codes.views.signup"

feeds = {
    'latest': LatestCommentFeed,
}


urlpatterns = patterns('',
#    url(r'^$', direct_to_template, {
#        "template": "homepage.html",
#    }, name="home"),
    url(r'^$','main.views.index',{},name="home"),
    
    url(r'^admin/invite_user/$', 'signup_codes.views.admin_invite_user', name="admin_invite_user"),
    url(r'^account/signup/$', signup_view, name="acct_signup"),
    
    (r'^about/', include('about.urls')),
    (r'^gear/', include('gear.urls')),
    (r'^manufacturer/', include('manufacturer.urls')),
    (r'^musician/', include('musician.urls')),
    (r'^musiciangear/', include('musiciangear.urls')),
    (r'^photos/', include('photo.urls')),
    (r'^account/', include('account.urls')),
    (r'^openid/(.*)', PinaxConsumer()),
    (r'^profiles/', include('basic_profiles.urls')),
    (r'^notices/', include('notification.urls')),
    (r'^announcements/', include('announcements.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),              
    (r'^threadedcomments/', include('threadedcomments.urls')),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
     {'feed_dict': feeds}),
    (r'^admin/(.*)', admin.site.root),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site_media/', include('staticfiles.urls')),
                            (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/rigs/uploads/'}),
    )
