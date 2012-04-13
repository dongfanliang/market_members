from django.db import models

class User(models.Model):
    username = models.CharField(max_length=60, primary_key=True)
    password = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'user'

