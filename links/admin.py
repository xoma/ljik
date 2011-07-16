# -*- coding: utf-8 -*-

from django.contrib import admin
from ljik.links.models import Link


class LinkAdmin(admin.ModelAdmin):
	list_display = ('id','title','url','description','author','creation_date','pub_date','user_status','access_level','status','can_comment')
	list_display_links = ('id','title',)
	list_editable  = ('user_status','status','access_level','can_comment')
	date_hierarchy = 'pub_date'
	fieldsets = (
		(u'Основная инофрмация',{'description':'Основная информация о ссылке','fields':('blog','title','url','description','link_source',)}),
		(u'Теги',{'description':u'Опишите ссылку метками','fields':('tags',)}),
		(u'Дополнительная информация',{'description':u'Дополнительная информация','fields':('user_status','pub_date','access_level','can_comment')}),		
		(u'Служебная информация',{'description':u'Служебная информация','fields': ('author','status',)}),
	)

admin.site.register(Link, LinkAdmin)
