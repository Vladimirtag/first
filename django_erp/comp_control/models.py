from django.db import models
from django.urls import *
from django.shortcuts import redirect
from django.db.models import Max
from django.utils import timezone
# Create your models here.


# class My(models.Model):
# 	name = models.CharField(max_length= 100)

# def remove_duplicated(model, fields):
# 	'Удаляет одинковые записа в таблице'
# 	duplicates = model.values(*fields)
# 	duplicates = duplicates.order_by()
# 	duplicates = duplicates.annotate(
# 		#Max вернет максимальный id, Count вернет количество объектов связаных через 'id'
# 		max_id = models.Max('id'), count_id=models.Count('id')
# 		)
# 	#вернет количест
# 	duplicates = duplicates.filter(count_id__gt=1)
# 	return duplicates


class Storage(models.Model):
	name = models.CharField(max_length = 200)
	date = models.DateTimeField('date_create')

	def __str__(self):
		return self.name


class WorkPlace(models.Model):
	name = models.CharField(max_length=200)
	storage = models.ForeignKey(Storage, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Box(models.Model):
	name = models.CharField(max_length=100)
	storage = models.ForeignKey(Storage, on_delete=models.CASCADE)

	def __str__(self):
		return "{0} | {1} ".format(self.name, self.storage )


class Component(models.Model):#Blog
	name = models.CharField(max_length=100, verbose_name = 'Part number')
	analog = models.ForeignKey("Component", on_delete=models.CASCADE, null=True, blank=True)
	number = models.IntegerField()
	article = models.CharField(max_length=100, verbose_name='Артикул', null=True, blank=True)
	count = models.IntegerField(verbose_name="Количество на складе", null=True)
	date_register = models.DateTimeField('date_create', null=True)
	package = models.ForeignKey("Package", on_delete=models.CASCADE, null=True, blank=True)
	box = models.ForeignKey(Box, on_delete=models.CASCADE, null=True, blank=True)
	# storage = models.ForeignKey(Storage, on_delete=models.CASCADE, null=True, blank=True)
	# unpuking = models.ForeignKey('UnPuking', on_delete=models.CASCADE, null=True, blank=True)
	counting = models.ForeignKey('Counting', on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Дата последнего поступлениея на склад')
	#value = models.ForeignKey("Values", on_delete=models.CASCADE, null=True, blank=True)
	type_ditail = models.ForeignKey("Type", on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Тип')
	unit = models.ForeignKey("Unit", on_delete=models.CASCADE, null=True, verbose_name = 'Единица измерения')

	def mycount(self):
		return '{0}'.format(self.count)


	def __str__(self):
		return "{0} | {1} ".format(self.number, self.name)

class Package(models.Model):
	type = models.CharField(max_length=100, verbose_name='Тип упаковки компонента')

	def __str__(self):
		return self.type

class Unit(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name



class Type(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class UnPuking(models.Model):
	description = models.CharField(max_length=100)
	time = models.DateTimeField('date_create')
	status = models.BooleanField(verbose_name="Что то не так", blank=True)
	responsible = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return '{0} | {1}'.format(self.description, self.time)


class Counting(models.Model):
	trabl = 'Ошибка'
	ok = "Ok"
	bu = ok, trabl
	time = models.DateTimeField('count_time')
	unpuking = models.ManyToManyField(UnPuking)
	status = models.BooleanField(bu)
	count = models.IntegerField()

	def __str__(self):
		return '{0}'.format(self.time)

class Position(models.Model):
	name =models.CharField(max_length=100)

	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	position = models.ForeignKey(Position, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class GroupComponents(models.Model):
	"""Комплектация для сборки"""
	name = models.CharField(max_length=100)
	number = models.CharField(max_length=50)
	components = models.ManyToManyField("QuantityComponent")
	plan = models.IntegerField('количество в производство', null=True, blank=True)


	def __str__(self):
		return self.name

class QuantityComponent(models.Model): #подсчитанные компоненты к прибору
	"""Класс в котором к каждому компоненту присваивется количество."""
	part_number = models.ForeignKey(Component, on_delete=models.CASCADE)
	quantity = models.IntegerField('quantity', null=True, blank=True)

	def complit(self):
		count = self.part_number.count
		return count

	def number(self):
		num = self.part_number.number
		return num

	# def save(self, *args, **kwargs):
	# 	summ = self.quantity * 10000
	# 	super(QuantityComponent, self).save(*args, **kwargs)
	# 	return summ

	def save(self):
		super(QuantityComponent, self).save()
		quantity_list = QuantityComponent.objects.all()
		for q_list in  quantity_list:
			if q_list.part_number == self.part_number:
				return redirect('/index/')



	# def get_absolute_url(self):
	# 	return "/quantity/%i/" % self.part_number

	# def save(self, *args, **kwargs):
	# 	self.quantity = self.quantity * 10
	# 	super(QuantityComponent, self).save(*args, **kwargs)

	def __str__(self):
		return '{0} _ | * quantity: {1}'.format(self.part_number, self.quantity)






class Device(models.Model):
	# name = models.CharField(max_length=100)
	serial_number = models.IntegerField('serial_number', null=True, blank=True)
	assembler = models.ForeignKey(User, on_delete=models.CASCADE)
	component = models.ForeignKey(GroupComponents, on_delete=models.CASCADE, verbose_name='Прибор')
	
	

	def __str__(self):
		return '{0}'.format(self.component)

class TrashComponents(models.Model):
	data = models.DateTimeField('date_create', auto_now_add=True, blank=True)
	user = models.ForeignKey('user', on_delete=models.CASCADE)
	write_off_ditail = models.ForeignKey('component', on_delete=models.CASCADE, blank=True)
	count_detail = models.IntegerField('количество списанных деталей', null=True, blank=True)
	write_off_group_ditail = models.ForeignKey('groupcomponents', on_delete=models.CASCADE, blank=True)
	count_group_detail = models.IntegerField('количество плат', null=True, blank=True)

	def __str__(self):
		return '{0}'.format(self.write_off_group_ditail)

	# def save(self, *args, **kwargs):
	# 	if not self.id:
	# 		self.data = timezone.now()
	# 	self.data = timezone.now()
	# 	return super(TrashComponents, self).save(*args, **kwargs)