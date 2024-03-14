# Generated by Django 5.0.3 on 2024-03-14 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoques', '0001_initial'),
        ('fornecedores', '0002_remove_fornecedor_produtos_fornecedor_produtos'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='fornecedor_FK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fornecedores.fornecedor'),
        ),
    ]