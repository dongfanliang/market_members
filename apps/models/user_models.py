from django.db import models

class User(models.Model):
    password = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=600, blank=True)
    extra = models.CharField(max_length=765, blank=True)
    branch = models.CharField(max_length=600, blank=True)
    branch_address = models.CharField(max_length=765, blank=True)
    username = models.CharField(max_length=60, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'user'

