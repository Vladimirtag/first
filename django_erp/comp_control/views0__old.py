from django.shortcuts import render, render_to_response
from comp_control.models import GroupComponents, Component, QuantityComponent
import xlrd, csv
from django.template import RequestContext, loader

# Create your views here.




def inbase(request):
	# file = xlrd.open_workbook('/home/vladimir/projects/python/django/django_erp/comp_control/sklad.xls')
	# sh = file.sheet_by_index(0)
	# numbrows = sh.nrows
	# my_list = ['detail_1']

	data = csv.reader(open('/home/vladimir/projects/python/django/django_erp/comp_control/sklad.csv'), delimiter = ',')
	for row in data:
		post = Component()
		post.name = row[3]
		if row[2]:
			post.article = row[2]
		# post.uni = row[4]
		if row[27]:
			post.count = row[27]
		post.number = row[0]
		post.save()
	return render(render, 'index.html')
	# return models.Component.object.bulk_create(load)


# def ddc_specification(request):
# 	data = csv.reader(open('/home/vladimir/projects/python/django/django_erp/comp_control/ColibriDDC_specific.csv'), delimiter = ',')
# 	quantity = 'rfwfwfe'


# 	# for row in data:
# 	# 	gcomp = models.GroupComponents()

# 		# for quantity in gcomp.components.all():
# 		# 	quantity = quantity.quantity
# 		# post.uni = row[4]
# 		# quantity.save()
# 	return render(render, 'index.html', {'quantity':quantity})
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# from django.db import models

# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     def __str__(self):              # __unicode__ on Python 2
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()

#     def __str__(self):              # __unicode__ on Python 2
#         return self.name

# class Entry(models.Model):
#     blog = models.ForeignKey(Blog)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()

#     def __str__(self):              # __unicode__ on Python 2
#         return self.headline


# e = Entry.objects.get(id=3) #имеет м2м на Author
# e.authors.all() # Returns all Author objects for this Entry.
# e.authors.count()
# e.authors.filter(name__contains='John')

# a = Author.objects.get(id=5)
# a.entry_set.all() # Returns all Entry objects for this Author.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# def getGroupComponents():
# 	count = []
#     group = []
#     data_components = []

#     q = GroupComponents.objects.all().filter(name='sdr4')
#     for qq in q: #получаю построчно Группы

#     	d = qq.components.all() #Вернет все Группы компонентов для QuantityComponent | Ныряем в
#     	for qua in d:
#     		qua

#     		# qua.quantity #получил количество компонентов для группы
#     		# for comp in qua:
#     		# 	comp1 = comp.part_number

#     		# count.append(qua) # компоненты для группы
#     		count.append(qua)
#     		data_components.append(qua)


# def ddc_specification(request):
#     context = {}
#     count = []
#     group = []
#     data_components = []

#     q = GroupComponents.objects.all().filter(name='sdr4')
#     for qq in q: #получаю построчно Группы

#     	d = qq.components.all() #Вернет все Группы компонентов для QuantityComponent | Ныряем в
#     	for qua in d:
#     		quas

#     		# qua.quantity #получил количество компонентов для группы
#     		# for comp in qua:
#     		# 	comp1 = comp.part_number

#     		# count.append(qua) # компоненты для группы
#     		count.append(qua)
#     		data_components.append(qua)






def ddc_specification(request):
    context = {}
    count = []
    group = []
    data_components = []

    q = GroupComponents.objects.all().filter(name='BOM_SDR_2')
    for qq in q: #получаю построчно Группы

    	d = qq.components.all() #Вернет все Группы компонентов для QuantityComponent | Ныряем в
    	count = (qua for qua in d)
    	# for qua in d:
    	# 	quantity
    	# 	count.append(qua)
    	# 	data_components.append(qua)

    	# 	# qua.quantity #получил количество компонентов для группы
    	# 	# for comp in qua:
    	# 	# 	comp1 = comp.part_number

    	# 	# count.append(qua) # компоненты для группы
    	# 	#git__hub

    # context['count'] = count.complit
    context['name'] = count
    context['group'] = q

    # context['group'] = q

    # return render(request, 'index.html', {"foo":"groupcomp"})
    return render_to_response("groupcomponents.html", context)
