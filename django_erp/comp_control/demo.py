


class Component(models.Model):#Blog
	name = models.CharField(max_length=100, verbose_name = 'Part number')
	analog = models.ForeignKey("Component", on_delete=models.CASCADE, null=True, blank=True)
	number = models.IntegerField()
	article = models.CharField(max_length=100, verbose_name='Артикул', null=True, blank=True)
	count = models.IntegerField(verbose_name="Количество на складе", null=True)

class QuantityComponent(models.Model): #подсчитанные компоненты к прибору
	"""Класс в котором к каждому компоненту присваивется количество."""
	part_number = models.ForeignKey(Component, on_delete=models.CASCADE)
	quantity = models.IntegerField('quantity', null=True, blank=True)

class Bom(models.Model):
	"""Комплектация для сборки"""
	name = models.CharField(max_length=100)
	# number = models.CharField(max_length=50)
	components = models.ManyToManyField("QuantityComponent")


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
					# for component in quantity_list: #QuantityComponent'ы ПАРЫ ОБЪЕКТЫ
					y = [q.part_number for q in quantity_list]
					# quantity_list_2 = Component.objects.filter(quantitycomponent__part_number = y[2] )
					for qc_object in quantity_list:
						qc_object

					forma_write_off.save()
					context['component_list'] = quantity_list
					context['component_2'] = qc_object
			return render(request, 'count_center.html', context)
	else:
		form = TrashComponentsForm()
	return render(request, 'choice_form.html', {'myforma':form})