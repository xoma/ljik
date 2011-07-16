# -*- coding: utf-8 -*-

from django.db import models

from ljik.core.models import Content
# Create your models here.

class Post(Content):
    
    title = models.CharField(u'заголовок',max_length=200,help_text=u'заголовок поста должен быть "говорящим"')
    text  = models.TextField(u'текст',help_text=u'введите текст вашей записи')

    def get_short_content(self):
        if '.' in self.text:
            return self.text.split('.')[0]
        return self.text

    def __unicode__(self):
        return self.title;

    class Meta(Content.Meta):
        verbose_name = u'запись'
        verbose_name_plural = u'записи'
