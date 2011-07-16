# -*- coding: utf-8 -*-

from django.contrib import admin
from ljik.core.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display  = ('id','owner','title','creation_date','description','status')
    list_editable = ('status',)
    fieldsets = (
        (u'Основная инофрмация',{'description':'Основная информация о блоге','fields':('owner','title','description','status')}),
        (u'Мета инофрмация (для поисковых машин)',{'description':'Мета инофрмация (для поисковых машин)','fields':('meta_keywords','meta_description',)}),
    )

admin.site.register(Blog, BlogAdmin)
