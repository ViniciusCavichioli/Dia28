# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 23:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0002_auto_20170828_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('sigla', models.CharField(max_length=10)),
                ('numero', models.CharField(max_length=10)),
                ('logo', models.CharField(max_length=10)),
                ('data_de_inicio', models.DateField(max_length=10)),
                ('data_de_fim', models.DateField(max_length=10)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='eventos.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('cpf', models.CharField(max_length=12)),
                ('mae', models.CharField(max_length=100)),
                ('pai', models.CharField(max_length=100)),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PessoaFisica', to='eventos.PessoaFisica'),
        ),
    ]
