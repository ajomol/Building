from django import forms

#custome imports
from building.models import BuildingGroup,BuildingDetails



class BuildingDetailsForm(forms.ModelForm):
	'''
	This is the form foir only creation
	'''
	class Meta:
		model = BuildingDetails
		exclude = ('is_status','created_on')

	def clean_build_name(s)
		build_name = self.request.POST.get('build_name')