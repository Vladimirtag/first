from django.shortcuts import render, render_to_response, redirect
from comp_control.models import GroupComponents, Component, QuantityComponent
import xlrd, csv
from django.template import RequestContext, loader
from comp_control.forms import GroupComponentsForm, TrashComponentsForm, TrashTouComponentsForm, MyForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

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
	# return models.Component.object.bulk_create(load)






#Обрабтываем форму ComboBox с именами устройств
# def get_boms(request):#/boms/
# 	if request.method == 'GET':
# 		form = GroupComponentsForm(request.GET)
		
# 			# device = form.cleaned_data['write_off_group_ditail']
# 		items = form.cleaned_data['count_group_detail']
# 		return HttpResponseRedirect('/bomlist/%s/rgerger' %  ( items))# multipleform = writeoff(request))

# 	else:
# 		form = GroupComponentsForm()
# 		return render(request, 'comboform.html', {'ComboBoms':form})

# def getMyParam(param):


def jsres(request):
	response = {'QuantityComponent':[{
		# {'part_number': q.part_number,
		'quantity': q.quantity} for q in QuantityComponent.objects.all() 
	]}
	return response

def forma(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		context = {}
		if form.is_valid():
			context['device'] = form.cleaned_data['write_off_group_ditail']
			context['count'] = form.cleaned_data['count_group_detail'] 
			mnoj = form.cleaned_data['count_group_detail']
			device = context['device']
			quantityGroup = QuantityComponent.objects.filter(groupcomponents__name__contains = device)
			context['group_device'] = quantityGroup
			if 	context['device'] == None or context['count'] == None:
				form = MyForm()
				return render(request, 'choice_form.html', {'myforma':form})
			
			mnoj_result = []
			balance = []
			sklad = []
			for qGroup in quantityGroup:
				mnoj_result.append(qGroup.quantity * mnoj)

			for q in quantityGroup:
				sklad.append(q.part_number.count)
			
			pre_balance = zip(sklad, mnoj_result)	
			for x, y in pre_balance:
				balance.append(x - y)

			context['full'] = zip(quantityGroup, mnoj_result, balance)
			return render(request, 'count_center.html', context)
	else:
		form = MyForm()
	return render(request, 'choice_form.html', {'myforma':form})
			

def writeoff(request):#/boms/
	if request.method == 'POST':
		form = TrashTouComponentsForm(request.POST)
		if form.is_valid():
			bom_name = form.cleaned_data['write_off_group_ditail']#выбирем проверенные данные
			multiple = form.cleaned_data['count_group_detail']
			return redirect('/bomlist/{0}/{1}/'.format(bom_name, multiple))
	else:
		form = TrashTouComponentsForm()
	return render(request, 'groupcomponents.html', {'count_form':form})

def specification(request, bom_name):
    context = {}
    count = []
    group = []
    data_components = []
    # ComboBoms = []
	# if request.method =="POST":
	# 	form = GroupComponentsForm(request.POST)
		# if form.valid(): проверки можешь делать
    # multipleform = TrashComponentsForm()
    q = GroupComponents.objects.all().filter(name = bom_name)
    for qq in q: #получаю построчно Группы
    	d = qq.components.all() #Вернет все Группы компонентов для QuantityComponent | Ныряем в
    	count = (qua for qua in d)
    context['name'] = count
    context['group'] = q
    context['count_form'] = TrashTouComponentsForm(request.POST)

    # context['ComboBoms'] = GroupComponentsForm(request.POST)
    # context['MultiplForm'] = multipleform
    # context['release'] = multipleform.count()

    return render(request, "groupcomponents.html", context)


def countspecification(request, device, multiple):
    if request.method=='GET':
        form = TrashComponentsForm(request.POST)
        context = {}
        quantityGroupComponentsForDevice = QuantityComponent.objects.filter(groupcomponents__name__contains = device)
        context['result'] = quantityGroupComponentsForDevice
        if form.is_valid():
            parameter = form.cleaned_data.get('write_off_group_ditail')
            # summ = quantityGroupComponentsForDevice.multiple(parameter
            context['parameter'] = parameter

    return render(request, "groupcomponents.html", context)
