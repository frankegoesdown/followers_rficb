from django.contrib import admin
from django import forms

from followers.models import Man, Follow


class ManAdmin(admin.ModelAdmin):
    list_display = ('name', 'len_follows', 'len_followed_by')
    list_display_links = ('name',)
    # inlines = [FollowsInline, FollowedInline]

    filter_horizontal = ['follow']

    def follows(self, obj):
        '''returns list of Men, whom obj follows'''
        return Follow.objects.filter(from_man_id=obj)

    def len_follows(self, obj):
        return str(len(self.follows(obj)))

    def followed_by(self, obj):
        '''returns list of Men, who follow obj'''
        return Follow.objects.filter(to_man_id=obj)

    def len_followed_by(self, obj):
        return str(len(self.followed_by(obj)))


admin.site.register(Man, ManAdmin)
