# -*- coding: utf-8 -*-
from django.contrib import admin
from ljik.quotes.models import Quote


class QuoteAdmin(admin.ModelAdmin):
	list_display = ('id','text','author','source','creation_date','pub_date','user_status','access_level','status','can_comment')
	list_display_links = ('id','text',)
	list_editable  = ('user_status','status','access_level','can_comment','source')
	date_hierarchy = 'pub_date'	
	fieldsets = (
		 (u'Основная информация',{'description':u'Основные данные цитаты','fields': ('blog','text','description','source','link_source',)}),
		 (u'Теги',{'description':u'Опишите цитату метками','fields':('tags',)}),
		 (u'Дополнительная информация',{'description':u'Дополнительная информация','fields':('user_status','pub_date','access_level','can_comment')}),		 
		 (u'Служебная информация',{'description':u'Служебная информация','fields': ('author','status',)}),
	)

admin.site.register(Quote, QuoteAdmin)
