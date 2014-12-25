# -*- coding: utf-8 -*-
# django
from django.db import models
# Create your models here.
class Users(models.Model):
	'''
	Description of users
	'''
	name = models.CharField(max_length=32)
	follow_ids = models.TextField()

	class Meta:
		db_table = u'users'

		def __str__(self):	# __unicode__ on Python 2
			return self.name

class Follow(models.Model):
	'''
	Description of followers
	'''
	uid = models.IntegerField()
	follow_uid = models.IntegerField()

	class Meta:
		db_table = 'user_follow'



