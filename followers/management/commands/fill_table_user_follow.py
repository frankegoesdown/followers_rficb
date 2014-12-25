# -*- coding: utf-8 -*-
# python
from optparse import make_option
# django
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
# followers
from followers.models import Users, Follow

class Command(BaseCommand):
	'''
	Fill table: user_follow
	'''
	def handle(self, *args, **options):
		users = Users.objects.all()
		#u_id = Users.objects.get(id=id)
		# iterate all users
		for user in users:
			if not user.follow_ids:
				continue
			# get followers list
			followers_id_list = user.follow_ids.split(' ')
			# iterate all followers
			for follower_id in followers_id_list:
				try:
					follow_uid = Users.objects.get(pk=follower_id)
				except ObjectDoesNotExist:
					#show exception in promt
					self.stdout.write('Wrong follower id=%s, for uid: %s\n' % (follower_id, user.id))
					continue
				try:
					foll = Follow(uid = user.id, follow_uid = follower_id)
					foll.save()
					self.stdout.write('Add follower id=%s, for user: %s\n'% (follower_id, user.id))
				except:
					#show exception in promt
					self.stdout.write('Already exist follower id=%s, for user: %s\n' % (follower_id, user.id))
					continue
		# show end in promt
		self.stdout.write('Cycle end.\n')