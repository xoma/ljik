# -*- coding: utf-8 -*-

from django.contrib import admin
from ljik.work.models import Work


class WorkAdmin(admin.ModelAdmin):
	list_display = ('id','author','creation_date','description','priority','pub_date','user_status','access_level','status','can_comment')
	list_display_links = ('id','description')
	list_editable  = ('priority','user_status','status','access_level','can_comment',)
	date_hierarchy = 'pub_date'	
	fieldsets = (
		(u'Основная инофрмация',{'description':u'Основная информация','fields':('blog','description','priority','deadline','is_do',)}),
		(u'Теги',{'description':u'Опишите ссылку метками','fields':('tags',)}),
		(u'Дополнительная информация',{'description':u'Дополнительная информация','fields':('user_status','pub_date','access_level','can_comment')}),		
		(u'Мета информация',{'description':u'Мета информация для поисковиков','fields':('meta_keywords','meta_description',)}),		
		(u'Служебная информация',{'description':u'Служебная информация','fields': ('author','status',)}),
	)



admin.site.register(Work, WorkAdmin)
