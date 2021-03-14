from django.db import models
from django.utils.translation import gettext_lazy as _


class Area(models.Model):
    administrative_zones = (
        ("S", "Sul"),
        ("N", "Norte"),
        ("L", "Leste"),
        ("O", "Oeste"),
        ("G", "Guarnição"),
        ("F", "Fora da Guarnição"),
    )
    area = models.CharField(
        max_length=1, choices=administrative_zones, verbose_name=_("Área")
    )
    descricao = models.CharField(
        max_length=50, verbose_name=_("Descrição"), unique=True
    )

    def __str__(self):
        return f"{self.area} - {self.descricao}"


class SubUnidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.sigla} - {self.nome}"


class PostoGraduacao(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    sigla = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.sigla} - {self.nome}"


class Militares(models.Model):

    identidade = models.CharField(max_length=11)
    nome = models.CharField(max_length=200)
    graduacao = models.ForeignKey(
        PostoGraduacao,
        verbose_name=_("Posto/Graduação"),
        on_delete=models.PROTECT,
    )
    subunidade = models.ForeignKey(
        SubUnidade, verbose_name=_("Subunidade"), on_delete=models.PROTECT
    )
    operacional = models.BooleanField(verbose_name=_("Operacional"))
    telefone = models.CharField(max_length=20)
    telefone_familia = models.CharField(
        max_length=20, verbose_name="Telefone de Familiar", blank=True
    )
    telefone_telegram = models.CharField(
        max_length=20, verbose_name="Telegram"
    )
    telefone_whatsapp = models.CharField(
        max_length=20, verbose_name="Whatsapp", blank=True
    )
    chamador = models.BooleanField(verbose_name=_("Chamador"))
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, verbose_name="UF")
    cep = models.IntegerField()
    area = models.ForeignKey(
        Area, verbose_name=_("Área"), on_delete=models.PROTECT
    )
    data_insercao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.graduation}"
