# -*- coding: utf-8 -*-
from django.db import models

class News(models.Model):
    title = models.CharField('Title', max_length=255)
    text = models.TextField(verbose_name='Tresc')
    posted_date = models.DateTimeField('Data dodania', auto_now_add=True)

    class Meta:
        verbose_name = "news"

    def __unicode__(self):
        return self.title