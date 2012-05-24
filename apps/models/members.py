from django.db import models
class Members(models.Model):
    id = models.IntegerField(primary_key=True)
    member_name = models.CharField(max_length=60, blank=True)
    members_id = models.CharField(max_length=60, db_column='members_ID', blank=True) # Field name made lowercase.
    member_phone = models.CharField(max_length=60, blank=True)
    member_create_time = models.DateField(null=True, blank=True)
    member_end_time = models.DateField(null=True, blank=True)
    member_surplus = models.FloatField(null=True, blank=True)
    member_total = models.FloatField(null=True, blank=True)
    member_points = models.IntegerField(null=True, blank=True)
    member_password = models.CharField(max_length=30, blank=True)
    member_card_id = models.CharField(max_length=30, blank=True)
    member_sex = models.CharField(max_length=30, blank=True)
    member_rank = models.CharField(max_length=30, blank=True)
    member_status = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'members'
