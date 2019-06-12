from django import forms

from . import models

from dal import autocomplete




class UpLoadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()


class CuanityComponentForm(forms.ModelForm):
	class Meta:
		model = models.QuantityComponent
		fields = ('part_number', "quantity")
		widgets = {
            'test': autocomplete.ModelSelect2()
        }


FIELD_NAME_MAPPING = {'number': 'Номер', 'number_action': 'сколько'}
class ComponentForms(forms.ModelForm):

	# article = forms.CharField(widget = forms.TextInput)#Можешь поставить любой виджет для Text

	def __init__(self, *args, **kwargs):
		super(ComponentForms, self).__init__(*args, **kwargs)

	def delete(self):
		pass

	def save(self):
		obj = super(ComponentForms, self).save(commit = False)
		if commit:
			obj.name = self.cleaned_data['name']
		# obj.analog = self.cleaned_data['analog']
			obj.count = self.cleaned_data['count']


	class Meta:
		model = models.Component
		fields = ['number', 'number_action', 'action']
		# exclude = ['unit']
		# widgets = {
  #           'article': autocomplete.ModelSelect2(url='country-autocomplete')
  #       }
	def add_prefix(self, field_name):
  		field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
  		return super(ComponentForms, self).add_prefix(field_name)

class GroupComponentsForm(forms.ModelForm):
	# id = forms.IntegerField(required=False, widget=forms.HiddenInput())
	class Meta:
		model = models.TrashComponents
		# model = models.Device
		fields = ['count_group_detail'] #'count_group_detail'

class TrashComponentsForm(forms.ModelForm):
	
	class Meta:
		model = models.TrashComponents
		# fields = ("__all__")
		fields = ['user', 'count_group_detail', 'write_off_group_ditail']
		# widgets = {
            
  #           'write_off_group_ditail': forms.CheckboxSelectMultiple(),

  #       }

		# widgets = {'check': forms.CheckboxSelectMultiple}













