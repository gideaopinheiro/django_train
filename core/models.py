from django.db import models
from django_countries.fields import CountryField
from markdownx.models import MarkdownxField
from slugify import slugify


class Person(models.Model):
    nomeCompleto = models.CharField(blank=True, null=True)
    nome = models.CharField(max_length=256, blank=True, null=True)

    aniversario = models.DateField(blank=True, null=True, verbose_name="aniversário")
    cargo = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField(max_length=200, blank=True, null=True)
    sitePessoal = models.URLField(blank=True, null=True, verbose_name="site pessoal")
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    slug = models.CharField(unique=True, blank=True, null=True)
    descricao = MarkdownxField(blank=True, null=True, verbose_name="descrição")
    email = models.EmailField(blank=True, null=True, verbose_name="e-mail")
    pais = CountryField(blank=True, null=True, verbose_name="país")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome if self.nome else str(self.id)