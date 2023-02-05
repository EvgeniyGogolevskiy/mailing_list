# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
