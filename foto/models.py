# -*- coding: utf-8 -*-

from django.db import models

from ljik.core.models import Content

# Create your models here.

class Foto(Content):
	url = models.URLField(u'url')
	description = models.TextField(u'описание')
	
	class Meta(Content.Meta):
		verbose_name=u'фото'
		verbose_name_plural=u'фотографии'
