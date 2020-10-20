from django.forms import ModelForm
from django import forms

from myapp.models import Hospede, Compositor, Musica


class HospedeForm(ModelForm):
	class Meta:
		model = Hospede
		fields = '__all__'


class CompositorForm(ModelForm):
	class Meta:
		model = Compositor
		fields = '__all__'
		widgets = {
			'data_nasc': forms.DateInput(
				attrs={
					'type': 'date',
					}
				)
			}


class MusicaForm(ModelForm):
	class Meta:
		model = Musica
		fields = '__all__'
		widgets = {
			'data': forms.DateInput(
				attrs={
					'type': 'date',
					}
			)
		}
