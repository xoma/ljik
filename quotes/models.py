# -*- coding: utf-8 -*-

from django.db import models
from ljik.core.models import Content

# Create your models here.

class Quote(Content):
    text   = models.TextField(u'текст',help_text=u'Введите текст цитаты')
    source = models.CharField(u'источник',max_length=200,help_text=u'Укажите источник цитаты')
    description = models.TextField(u'Описание',max_length=200,help_text=u'Пояснение к цитате',blank=True)
	
    def __unicode__(self):
        return '%s...' % self.text[0:30]

    class Meta(Content.Meta):
        verbose_name=u'цитата'
        verbose_name_plural=u'цитаты'

	
