# -*- coding: utf-8 -*-
# django
from django.contrib import admin
from django import forms
# Register your models here.
from followers.models import Users, Follow

class FollowsInline(admin.TabularInline):
	model = Follow
	fk_name = "user"

class FollowedInline(admin.TabularInline):
	model = Follow
	fk_name = "follow_user"

class UsersAdmin(admin.ModelAdmin):
	'''
	Show count pursues and followers of users
	'''
	list_display = ('name', 'count_pursues', 'count_followers')
	list_display_links = ('name',)
	inlines = [FollowsInline, FollowedInline]

	# Get pursues
	def pursues(self,obj):
		return Follow.objects.filter(user_id=obj)

	# Return count of pursues
	def count_pursues(self,obj):
		return str(len(self.pursues(obj)))

	# Get followers
	def followers(self,obj):
		return Follow.objects.filter(follow_user_id=obj)

	# Return count of followers
	def count_followers(self,obj):
		return str(len(self.followers(obj)))

class FollowersAdmin(admin.ModelAdmin):
	list_display = ('name', 'count_followers')
	list_display_links = ('name',)
	inlines = [FollowsInline, FollowedInline]

	def count_followers(self,obj):
		return len(obj.follow_ids.split(" "))
	count_followers.allow_tags = True


admin.site.register(Users, UsersAdmin)