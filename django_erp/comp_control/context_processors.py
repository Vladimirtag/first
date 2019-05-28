from django import forms
from . import models
from django.shortcuts import render, render_to_response, redirect


# class GroupComponentsForm(forms.ModelForm):
# 	# id = forms.IntegerField(required=False, widget=forms.HiddenInput())
# 	class Meta:
# 		model = models.Device
# 		fields = ["component"]





# def get_boms_processor(request):#/boms/
# 	if request.method == 'POST':
# 		form = GroupComponentsForm(request.POST)
# 		if form.is_valid():
# 			name = form.cleaned_data['component']
# 			return redirect('/bomlist/{0}/'.format(name))
# 	else:
# 		form = GroupComponentsForm()
# 	return {'ComboBomsProcessor':form}












