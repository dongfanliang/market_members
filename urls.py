from django.conf.urls.defaults import patterns, include, url
import settings

from apps.user import user_views
from apps.user import members_views
from apps.user import rule_views


urlpatterns = patterns('',
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
     url(r'^$', user_views.log_in),
     url(r'^login/$', user_views.log_in,name="login"),
     url(r'^logout/$', user_views.log_out),
     url(r'^index/$', user_views.index, name="index"),
     url(r'^user/$', user_views.user_list, name="users"),
     url(r'^user/getpassword/$', user_views.getpassword, name="getpassword"),
     url(r'^user/add/$', user_views.user_add, name="useradd"),
     url(r'^user/info/$', user_views.userinfo, name="userinfo"),
     url(r'^user/delete/$', user_views.user_delete, name="userdelete"),
     url(r'^user/search/$', user_views.user_search, name="usersearch"),

     #url(r'^user/info/$', user_views.edit_info, name="editinfo"),
     url(r'^members/$', members_views.members_list, name="members"),
     url(r'^cards/$', members_views.cards_list, name="cards"),
     url(r'^cards/retroactive/$', members_views.cards_retroactive, name="cardsretroactive"),
     url(r'^cards/search/$', members_views.cards_search, name="cardssearch"),
     url(r'^cards/loss/$', members_views.cards_loss, name="cardsloss"),
     url(r'^cards/v/$', members_views.cards_v, name="cardsv"),
     url(r'^cards/consume/$', members_views.cards_consume, name="cardsconsume"),
     url(r'^cards/s/$', members_views.cards_s, name="cardss"),
     url(r'^cards/ss/$', rule_views.cards_ss, name="cardsss"),

#     url(r'^members/cards/status/$', members_views.members_cards_status, name="memberscardsstatus"),
     url(r'^cards/recharge/$', members_views.cards_rechange, name="cardsrechange"),
     url(r'^members/register/$', members_views.members_register, name="memregister"),
     url(r'^members/delete/$', members_views.members_delete, name="delmembers"),
     url(r'^members/edit/$', members_views.members_edit, name="editmembers"),
     url(r'^members/serach/$', members_views.members_search, name="searchmembers"),
     url(r'^members/rule/$', members_views.member_rule, name="memrule"),
     url(r'^rule/$', rule_views.proportion, name="pointsrule"),
     url(r'^rule/edit/$', rule_views.proportion_edit, name="proportionedit"),
     url(r'^rule/delete/$', rule_views.proportion_delete, name="proportiondelete"),
     url(r'^rule/rank/$', rule_views.rank_set, name="rank"),
     url(r'^rule/proportion/$', rule_views.proportion_add, name="proportionadd"),
     url(r'^gift/$', rule_views.gift_list, name="gift"),
     url(r'^gift/points/$', rule_views.point_gift, name="pointgift"),
     url(r'^gift/add/$', rule_views.gift_add, name="giftadd"),
     url(r'^gift/delete/$', rule_views.gift_delete, name="giftdelete"),
     url(r'^gift/edit/$', rule_views.gift_edit, name="giftedit"),
     #url(r'^admininfo/$', user_views.register, name="admininfo"),
)
