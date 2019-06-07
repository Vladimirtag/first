from django.contrib import admin

# Register your models here.
from . import models
from . import forms
# from comp_control.widgets import RichTextEditorWidget

class ComponentAdmin(admin.ModelAdmin):
	list_display=('number', 'name', 'article', 'count', 'type_ditail')
	search_fields = ('number', 'name')
	list_filter = ('type_ditail',)
	list_editable = ('count',)
	actions = ('name',)
	# formfield_overrides = { models.TextField: {'widget': RichTextEditorWidget}, }
	form = forms.ComponentForms #ссылка на мою форму


# class BoxInLine(admin.StackedInline):
# 	model = models.Box
# 	extra = 10


class GroupComponentsAdmin(admin.ModelAdmin):
	filter_horizontal = ('components',)
	# inlines = [BoxInLine]

class QuantityComponentAdmin(admin.ModelAdmin):
	search_fields = ('number', 'name')
	form = forms.CuanityComponentForm


class TrashComponentsAdmin(admin.ModelAdmin):
	list_display = ('write_off_group_ditail', 'data', 'count_group_detail', 'user')




admin.site.register(models.Storage)
admin.site.register(models.WorkPlace)
admin.site.register(models.Box)
admin.site.register(models.Component, ComponentAdmin)
admin.site.register(models.UnPuking)
admin.site.register(models.Position)
admin.site.register(models.User)
admin.site.register(models.Counting)
admin.site.register(models.Device)
admin.site.register(models.GroupComponents, GroupComponentsAdmin)
admin.site.register(models.QuantityComponent, QuantityComponentAdmin)
# admin.site.register(models.My)
admin.site.register(models.Type)
admin.site.register(models.Unit)
admin.site.register(models.Package)
admin.site.register(models.TrashComponents, TrashComponentsAdmin)


# class ComponentAdmin(admin.ModelAdmin):
# 	fields = ('unit')

admin.AdminSite.site_header = "Учет ресурсов"


# class ComponentAdmin(admin.ModelAdmin):
# 	list_display = ('id')