from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64L)
    email = models.CharField(max_length=64L)
    phone = models.CharField(max_length=64L)
    validated = models.BooleanField(default=False)
    location = models.CharField(max_length=64L, null=True, blank=True)
    description = models.CharField(max_length=640L, null=True, blank=True)
    user_type = models.IntegerField(default=0)
    referral_id = models.CharField(max_length=64L, null=True, blank=True)
    class Meta:
        db_table = 'user'

class Referral(models.Model):
    user = models.ForeignKey('User')
    referral_id = models.CharField(max_length=64L)
    status = models.IntegerField(default=0)
    class Meta:
        db_table = 'referral'
