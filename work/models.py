# -*- coding: utf-8 -*-

from django.db import models

from ljik.core.models import Content
# Create your models here.


class Work(Content):
	IS_NOT_DO = 0
	IS_DO         = 1
		
	PRIORITY_LOW       = 0
	PRIORITY_NORMAL = 1
	PRIORITY_FAST       = 2
	
	PRIORITY_TYPES = (
		(PRIORITY_LOW,u'низкий'),
		(PRIORITY_NORMAL,u'обычный'),
		(PRIORITY_FAST,u'высокий')
	)
	
	description = models.CharField(u'дело',max_length=400)
	priority       = models.SmallIntegerField(u'приоритет',choices=PRIORITY_TYPES,default=PRIORITY_NORMAL)
	deadline     = models.DateField(u'выполнить до')
	is_do          = models.BooleanField(u'сделано',default=IS_NOT_DO)
	
	def __unicode__(self):
		return self.description
	
	class Meta:
		ordering = ('creation_date',)
		verbose_name = u'задача'
		verbose_name_plural = u'задачи'
