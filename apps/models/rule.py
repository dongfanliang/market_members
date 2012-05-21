from django.db import models

class Rank(models.Model):
    id = models.IntegerField(primary_key=True)
    ranka = models.IntegerField(null=True, db_column='rankA', blank=True) # Field name made lowercase.
    rankb = models.IntegerField(null=True, db_column='rankB', blank=True) # Field name made lowercase.
    rankc = models.IntegerField(null=True, db_column='rankC', blank=True) # Field name made lowercase.
    class Meta:
       db_table = u'rank'

class Proportional(models.Model):
    id = models.IntegerField(primary_key=True)
    goodstype = models.CharField(max_length=150, blank=True)
    proportion = models.CharField(max_length=60, blank=True)
    extra = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'proportional'

class Gift(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    price = models.CharField(max_length=30, blank=True)
    points = models.CharField(max_length=30, blank=True)
    rank = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'gift'

