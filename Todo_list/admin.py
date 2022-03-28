from django.contrib import admin
from .models import TodoModel
# Register your models here.
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
    
# class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
# 	model = TodoModel
	
@admin.register(TodoModel)
class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
	# show jalali date in list display 
	list_display = ['__str__']
	# inlines = (MyInlines1,)
	# raw_id_fields = ('user', )
	# readonly_fields = ('user', 'date',)
	
	def get_created_jalali(self, obj):
		return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')
	
	get_created_jalali.short_description = 'تاریخ ایجاد'
	get_created_jalali.admin_order_field = 'created'