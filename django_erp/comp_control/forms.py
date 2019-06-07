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


class ComponentForms(forms.ModelForm):

	article = forms.CharField(widget = forms.TextInput)#Можешь поставить любой виджет для Text

	class Meta:
		model = models.Component
		fields = ("__all__")
		# exclude = ['unit']
		widgets = {
            'article': autocomplete.ModelSelect2(url='country-autocomplete')
        }


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













