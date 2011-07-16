# -*- coding: utf-8 -*-
from datetime import datetime

from taggit.managers import TaggableManager

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    ACTIVE  = 1
    DELETED = 0
    BLOG_STATUSES = (
        (ACTIVE,u'активен'),
        (DELETED,u'удален')
    )
    owner = models.ForeignKey(User,verbose_name=u'автор',help_text=u'владелец блога')
    title = models.CharField(u'название блога',max_length=150,help_text=u'укажите название блога')
    description = models.TextField(u'Описание блога',blank=True,help_text=u'опишите свой блог')
    creation_date = models.DateTimeField(u'дата создания',auto_now_add=True)
    change_date  = models.DateTimeField(u'дата изменеия',auto_now=True)
    meta_description = models.TextField(u'описание',help_text=u'введите описание для вашей записи (для поисковиков)',blank=True)
    meta_keywords  = models.TextField(u'ключевые слова',help_text=u'введите ключевые слова для вашей записи (для поисковиков)',blank=True)
    status       = models.IntegerField(u'статус',choices=BLOG_STATUSES,default=ACTIVE)
            

    def __unicode__(self):
        return  "%s (%s)" % (self.title,self.owner.username)

    class Meta:
        ordering = ('creation_date',)
        verbose_name = u'блог'
        verbose_name_plural = u'блоги'


class PublicManager(models.Manager):
    def get_query_set(self):
        return  super(PublicManager,self).get_query_set().filter(
                status=Content.STATUS_ACTIVE,
                user_status=Content.USER_STATUS_PUBLISH_NOW,
                access_level=Content.ACCESS_ALL
        )



class Content(models.Model):

    default_keywords = u'ljik.ru, блоги, видео, цитаты, сообщения, сообщества, заметки, напоминания'

    default_description = u'ljik.ru - заведите свой блог, делитесь записями, публикуйте видео и оставляйте заметки'

    STATUS_ACTIVE     = 1
    STATUS_DELETED    = 0
    STATUS_NOT_VERIFY = -1

    STATUS_TYPES = (
        (STATUS_ACTIVE,u'доступно'),
        (STATUS_DELETED,u'удалено'),
        (STATUS_NOT_VERIFY,u'на проверке'),
    )

    ACCESS_PRIVATE = 0
    ACCESS_ALL     = 1
    ACCESS_FRIENDS = 2

    ACCESS_TYPES = (
        (ACCESS_PRIVATE,u'только мне'),
        (ACCESS_ALL,u'всем'),
        (ACCESS_FRIENDS,u'только друзьям'),
    )

    USER_STATUS_PUBLISH_NOW  = 1
    USER_STATUS_PUBLISH_LATE = 2
    USER_STATUS_DRAFT        = 3

    USER_STATUS_TYPES = (
        (USER_STATUS_PUBLISH_NOW,u'опубликовать сейчас'),
        (USER_STATUS_PUBLISH_LATE,u'опубликовать позже'),
        (USER_STATUS_DRAFT,u'сохранить как черновик'),
    )

    author   = models.ForeignKey(User,verbose_name=u'автор',help_text='укажите автора')
    blog     = models.ForeignKey(Blog,verbose_name=u'блог',help_text=u'укажите блог, в котором публикуете материал')
    pub_date = models.DateTimeField(u'дата публикации',blank=True,default=datetime.now(), help_text='опубликовать сейчас или позже')
    creation_date = models.DateTimeField(u'дата создания',auto_now_add=True)
    change_date  = models.DateTimeField(u'дата изменеия',auto_now=True)
    access_level = models.SmallIntegerField(u'доступ',choices=ACCESS_TYPES,default=ACCESS_ALL,help_text='укажите кто будет видеть Вашу запись')
    can_comment = models.BooleanField(u'комментиарии',default=True,help_text=u'разрешите комментарии для записи')
    status = models.SmallIntegerField(u'системный статус',choices=STATUS_TYPES,default=STATUS_ACTIVE,help_text='укажите доступна ли запись на сайте')
    user_status = models.SmallIntegerField(u'статус',choices=USER_STATUS_TYPES,default=USER_STATUS_PUBLISH_NOW,help_text=u'статус записи')
    link_source = models.URLField(u'источник (ссылка)',verify_exists=False,blank=True,help_text=u'источник (ссылка на интернет-ресурс)')
    meta_description = models.TextField(u'описание',help_text=u'введите описание для вашей записи (для поисковиков)',blank=True)
    meta_keywords  = models.TextField(u'ключевые слова',help_text=u'введите ключевые слова для вашей записи (для поисковиков)',blank=True)
    tags = TaggableManager()
    objects = models.Manager()
    public  = PublicManager()


    def get_meta_keywords(self,default=''):
        if self.meta_keywords:
            return self.meta_keywords
        elif default:
            return default
        else:
            return self.default_keywords

    def get_meta_description(self,default=''):
        if self.meta_description:
            return self.meta_description
        elif default:
            return default
        else:
            return self.default_description


    def get_meta(self):
        return {'keywords':self.get_meta_keywords(),'description':self.get_meta_description()}

    class Meta:
        abstract = True
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'







