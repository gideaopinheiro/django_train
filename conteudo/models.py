from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='autor')
    materia = models.CharField(max_length=250, verbose_name='matéria')
    assunto = models.CharField(max_length=250, verbose_name='assunto')
    topico = models.CharField(max_length=250, verbose_name='tópico')
    titulo = models.CharField(max_length=250,  verbose_name='título')
    dataPublicacao = models.DateTimeField(default=timezone.now, verbose_name='data de publicação')
    texto = models.TextField()

    class Meta():
        verbose_name_plural = 'Posts'

    def __str__(self):
        return '{}: {} - {}'.format(self.autor, self.assunto, self.topico)