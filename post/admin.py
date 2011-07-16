# -*- coding: utf-8 -*-

from django.contrib import admin
from ljik.post.models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ('id','text','author','creation_date','pub_date','user_status','access_level','status','can_comment')
	list_display_links = ('id','text',)
	list_editable  = ('user_status','status','access_level','can_comment',)
	date_hierarchy = 'pub_date'	
	fieldsets = (
		(u'Основная инофрмация',{'description':u'Основная информация','fields':('blog','title','text','link_source',)}),
		(u'Теги',{'description':u'Опишите ссылку метками','fields':('tags',)}),
		(u'Мета информация',{'description':u'Мета информация для поисковиков','fields':('meta_keywords','meta_description',)}),
		(u'Дополнительная информация',{'description':u'Дополнительная информация','fields':('user_status','pub_date','access_level','can_comment')}),		
		(u'Служебная информация',{'description':u'Служебная информация','fields': ('author','status',)}),
	)



admin.site.register(Post, PostAdmin)
