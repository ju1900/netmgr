from django.contrib import admin
from testlist.models import *

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ('name',)

class ChapterModelAdmin(admin.ModelAdmin):
    list_display = ('sequence', 'title', 'product')
    search_fields = ('title', 'product') 

class SectionModelAdmin(admin.ModelAdmin):
    list_display = ('sequence', 'title', 'chapter')
    search_fields = ('title', 'chapter',)

class TestplanModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'engineer', 'created', 'modified')
    list_filter = ('engineer',)
    search_fields = ('title', 'engineer',)
    
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.engineer = request.user
        obj.save()

class BugModelAdmin(admin.ModelAdmin):
    list_display = (
        'product', 
        'sequence',
        'title',
        'priority',
        'severity',
        'status',
        'engineer',
    )
    list_filter = (
        'product', 
        'priority',
        'severity',
        'status',
        'engineer',
    )
    search_fields = ('product', 'title',)
    
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.engineer = request.user
        obj.save()

class TestcaseModelAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'support', 
        'priority',
        'result',
        'engineer',
        'section',
        'finish',
    )
    list_filter = ( 
        'support', 
        'priority',
        'result',
        'finish',
    )
    search_fields = ('title',)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.engineer = request.user
        obj.save()

admin_register = (
    (Product, ProductModelAdmin), 
    (Chapter, ChapterModelAdmin), 
    (Section, SectionModelAdmin), 
    (Testplan, TestplanModelAdmin), 
    (Bug, BugModelAdmin), 
    (Testcase, TestcaseModelAdmin),
)

for register in admin_register:
    admin.site.register(*register)