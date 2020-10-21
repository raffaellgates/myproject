from django import forms
from django.forms import ModelForm

from myapp.models import Compositor, Constelacao, Estrela, Hospede, Musica


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


class EstrelaForm(ModelForm):
	class Meta:
		model = Estrela
		fields = '__all__'

	
class ConstelacaoForm(ModelForm):
	class Meta:
		model = Constelacao
		fields = '__all__'
