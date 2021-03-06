# Generated by Django 2.1.5 on 2019-02-03 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0002_auto_20190203_1316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='assunto',
            field=models.CharField(max_length=250, verbose_name='assunto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='dataPublicacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de publicação'),
        ),
        migrations.AlterField(
            model_name='post',
            name='materia',
            field=models.CharField(max_length=250, verbose_name='materia'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=250, verbose_name='título'),
        ),
        migrations.AlterField(
            model_name='post',
            name='topico',
            field=models.CharField(max_length=250, verbose_name='tópico'),
        ),
    ]
