from django.db import models


class Hospede(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Compositor(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome


class Musica(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    letra = models.TextField()
    compositores = models.ManyToManyField(
        Compositor, related_name='compositor')

    def __str__(self):
        return self.nome


class Estrela(models.Model):
    nome = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Constelacao(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    estrelas = models.ForeignKey(
        Estrela, related_name='contelacao', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
