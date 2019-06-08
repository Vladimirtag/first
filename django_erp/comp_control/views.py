from django.shortcuts import render, render_to_response, redirect
from comp_control.models import Bom, Component, QuantityComponent, TrashComponents
import xlrd, csv
from django.template import RequestContext, loader
from comp_control.forms import GroupComponentsForm, TrashComponentsForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.db.models import Count
# Create your views here.




def inbase(request):
	# file = xlrd.open_workbook('/home/vladimir/projects/python/django/django_erp/comp_control/sklad.xls')
	# sh = file.sheet_by_index(0)
	# numbrows = sh.nrows
	# my_list = ['detail_1']

	data = csv.reader(open('/home/vladimir/projects/python/django/mx_venv/django_erp/comp_control/sklad.csv'), delimiter = ',')
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

def jsres(request):
	response = {'QuantityComponent':[{
		# {'part_number': q.part_number,
		'quantity': q.quantity} for q in QuantityComponent.objects.all() 
	]}
	return response

def forma(request):
	if request.method == 'POST':
		form = TrashComponentsForm(request.POST)
		context = {}
		if form.is_valid():
			context['device'] = form.cleaned_data['write_off_group_ditail']
			context['count'] = form.cleaned_data['count_group_detail'] 
			mnoj = form.cleaned_data['count_group_detail']
			groupcomponents_id = Bom.objects.get(name=context['device'])#Нельзя нзывать одинаково производимые девайсы

			#покажи все QuantityComponents у которого имя Bom которое приходит из формы.
			#QuantityComponent это пара "" компонент и его количество ""
			quantityGroup = QuantityComponent.objects.filter(bom__id__contains = groupcomponents_id.id)
			context['count_quantity_group'] = quantityGroup.count()#возвращает количество записей
			if 	context['device'] == None or context['count'] == None:
				form = TrashComponentsForm()
				return render(request, 'choice_form.html', {'myforma':form})
			
			#Основные хранилища
			sklad = []       # на склде до списывания
			mnoj_result = [] # то, сколько будет нужно списать
			balance = []     # вывод результата до списывания
			save_total_balance = []
			for qGroup in quantityGroup:
				mnoj_result.append(qGroup.quantity * mnoj)

			for q in quantityGroup:
				sklad.append(q.part_number.count)
			
			pre_balance = zip(sklad, mnoj_result)	
			for x, y in pre_balance:
				balance.append(x - y)
			context['full'] = zip(quantityGroup, mnoj_result, balance)
			context['write_of_forma'] = form
			
			if 'write_off' in request.POST:
				form = TrashComponentsForm(request.POST)
				if form.is_valid():
					forma_write_off = form.save(commit = False)
					device = form['write_off_group_ditail']
					quantity_list = QuantityComponent.objects.all()#возьми все детали пары "имя/количество"" для инстанса Bom
					# quantity_obj = quantity_list.get(id = 1 )
					# components = quantity.filter()

					# for component in quantity_list: #QuantityComponent'ы ПАРЫ ОБЪЕКТЫ
					y = [q.part_number for q in quantity_list]
					# quantity_list_2 = Component.objects.filter(quantitycomponent__part_number = y[2] )


					for qc_object in quantity_list:
						# quantity_list_2 = Component.objects.get(quantitycomponent__part_number = qc_object.part_number )
						qc_object

					forma_write_off.save()
					# component = [q.part_number for q in quantity_list]
					# write_of_forma = form.save()
					# context['rrr'] = summ_detail
					context['component_list'] = quantity_list
					# context['component']=component
					context['component_2'] = qc_object
					# context['comp']=res
			return render(request, 'count_center.html', context)
	else:
		form = TrashComponentsForm()
	return render(request, 'choice_form.html', {'myforma':form})
			

def writeoff(request):#/boms/
	if request.method == 'POST':
		form = TrashComponentsForm(request.POST)
		if form.is_valid():
			bom_name = form.cleaned_data['write_off_group_ditail']#выбирем проверенные данные
			multiple = form.cleaned_data['count_group_detail']
			return redirect('/bomlist/{0}/{1}/'.format(bom_name, multiple))
	else:
		form = TrashComponentsForm()
	return render(request, 'groupcomponents.html', {'count_form':form})

def specification(request, bom_name):
    context = {}
    count = []
    group = []
    data_components = []
    q = Bom.objects.all().filter(name = bom_name)
    for qq in q: #получаю построчно Группы
    	d = qq.components.all() #Вернет все Группы компонентов для QuantityComponent | Ныряем в
    	count = (qua for qua in d)
    context['name'] = count
    context['group'] = q
    context['count_form'] = TrashComponentsForm(request.POST)
    return render(request, "groupcomponents.html", context)


def countspecification(request, device, multiple):
    if request.method=='GET':
        form = TrashComponentsForm(request.POST)
        context = {}
        quantityGroupComponentsForDevice = QuantityComponent.objects.filter(bom__name__contains = device)
        context['result'] = quantityGroupComponentsForDevice
        if form.is_valid():
            parameter = form.cleaned_data.get('write_off_group_ditail')
            # summ = quantityGroupComponentsForDevice.multiple(parameter
            context['parameter'] = parameter

    return render(request, "groupcomponents.html", context)


