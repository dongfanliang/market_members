from django.conf.urls.defaults import patterns, include, url
import settings

from apps.user import user_views
from apps.user import members_views


urlpatterns = patterns('',
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
     url(r'^$', user_views.log_in),
     url(r'^login/$', user_views.log_in),
     url(r'^logout/$', user_views.log_out),
     url(r'^index/$', user_views.index, name="index"),
     url(r'^members/$', members_views.members_list, name="members"),
     url(r'^members/register/$', members_views.members_register, name="memregister"),
     url(r'^members/delete/$', members_views.members_delete, name="delmembers"),
     #url(r'^members/edit/$', members_views.members_edit, name="editmembers"),
     #url(r'^admininfo/$', user_views.register, name="admininfo"),
)
