# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from followers.models import Users

admin.site.register(Users)
