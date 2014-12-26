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
		#managed = True
		db_table = u'users'
		ordering = ('id',)

		def __str__(self):	# __unicode__ on Python 2
			return self.name

class Follow(models.Model):
	'''
	Description of followers
	'''
	user = models.ForeignKey('Users', related_name='user')
	follow_user = models.ForeignKey('Users', related_name='follow_user')

	class Meta:
		db_table = 'user_follow'



