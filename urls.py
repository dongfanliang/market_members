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
     url(r'^user/$', user_views.user_list, name="users"),
     url(r'^user/add/$', user_views.user_add, name="useradd"),
     url(r'^user/info/$', user_views.userinfo, name="userinfo"),
     url(r'^user/delete/$', user_views.user_delete, name="userdelete"),
     url(r'^user/search/$', user_views.user_search, name="usersearch"),

     #url(r'^user/info/$', user_views.edit_info, name="editinfo"),
     url(r'^members/$', members_views.members_list, name="members"),
     url(r'^cards/$', members_views.cards_list, name="cards"),
     url(r'^cards/search/$', members_views.cards_search, name="cardssearch"),
     url(r'^cards/loss/$', members_views.cards_loss, name="cardsloss"),

#     url(r'^members/cards/status/$', members_views.members_cards_status, name="memberscardsstatus"),
     url(r'^cards/recharge/$', members_views.cards_rechange, name="cardsrechange"),
     url(r'^members/register/$', members_views.members_register, name="memregister"),
     url(r'^members/delete/$', members_views.members_delete, name="delmembers"),
     url(r'^members/edit/$', members_views.members_edit, name="editmembers"),
     url(r'^members/serach/$', members_views.members_search, name="searchmembers"),
     #url(r'^admininfo/$', user_views.register, name="admininfo"),
)
