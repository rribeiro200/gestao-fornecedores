# Generated by Django 5.0.3 on 2024-03-14 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0006_remove_fornecedor_produtos_fornecedor_produtos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='produtos',
        ),
    ]
