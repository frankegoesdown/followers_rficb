# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Users(models.Model):
    '''
    Description of users, get names
    '''
    name = models.CharField(u'Имя', max_length=32)

    class Meta:
        ordering = ('name',)

        def __str__(self):
            return self.name


class Follow(models.Model):
    '''
    Description of followers
    '''
    uid = models.ForeignKey('Users', related_name='uid')
    follow_uid = models.ForeignKey('Users', related_name='follow_uid')