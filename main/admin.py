# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'birthday', 'email')


admin.site.register(Subscriber, SubscriberAdmin)
