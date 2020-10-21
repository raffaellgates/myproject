from django.shortcuts import redirect, render

from myapp.forms import (CompositorForm, ConstelacaoForm, EstrelaForm,
                         HospedeForm, MusicaForm)
from myapp.models import Compositor, Constelacao, Estrela, Hospede, Musica


def list_hospedes(request):
    hospedes = Hospede.objects.all()
    return render(request, "list_hospedes.html", {'hospedes': hospedes})


def add_hospede(request):
    if request.method == "POST":
        form = HospedeForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_hospedes')
    else:
        form = HospedeForm()
        return render(request, "add.html", {'form': form})


def list_compositor(request):
    compositor = Compositor.objects.all()
    return render(request, "list_compositor.html", {'compositores': compositor})


def add_compositor(request):
    if request.method == "POST":
        form = CompositorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_compositores')
    else:
        form = CompositorForm()
        return render(request, "add.html", {'form': form})


def list_musica(request):
    musica = Musica.objects.all()
    return render(request, "list_musica.html", {'musicas': musica})


def add_musica(request):
    if request.method == "POST":
        form = MusicaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_musicas')
    else:
        form = MusicaForm()
        return render(request, "add.html", {'form': form})


def list_estrela(request):
    estrela = Estrela.objects.all()
    return render(request, "list_estrela.html", {'estrelas': estrela})


def add_estrela(request):
    if request.method == "POST":
        form = EstrelaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_estrelas')
    else:
        form = EstrelaForm()
        return render(request, "add.html", {'form': form})


def list_constelacao(request):
    constelacao = Constelacao.objects.all()
    return render(request, "list_constelacoes.html", {'constelacoes': constelacao})


def add_constelacao(request):
    if request.method == "POST":
        form = ConstelacaoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_constelacoes')
    else:
        form = ConstelacaoForm()
        return render(request, "add.html", {'form': form})
