# -*- coding: utf-8 -*-

from django.db import models
from ljik.core.models import Content

# Create your models here.

class Link(Content):
	title = models.CharField(u'заголовок',max_length=150,help_text=u'заголовок ссылки')
	url   = models.URLField(u'ссылка',max_length=150,help_text=u'ссылка')
	description = models.TextField(u'описание',help_text=u'описание ссылки',blank=True)
	
	def __unicode__(self):
		return self.title
	
	class Meta(Content.Meta):
		verbose_name = u'ссылка'
		verbose_name_plural = u'ссылки'

