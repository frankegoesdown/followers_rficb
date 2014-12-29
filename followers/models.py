# -*- coding: utf-8 -*-
#django
from django.db import models

class Man(models.Model):
	name = models.CharField(max_length=32)
	follow_ids = models.TextField()
	follow = models.ManyToManyField('self', symmetrical=False, related_name='followers',  db_table='followers_man_follow')

	class Meta:
		db_table = "followers_man"
		managed = True

	#show name and id of mans
	def __str__(self):				# __unicode__ on Python 2
		return "{0}, id={1}".format(self.name, self.id)
