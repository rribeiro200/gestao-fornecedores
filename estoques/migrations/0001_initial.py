# Generated by Django 5.0.3 on 2024-03-14 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id_estoque', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField()),
                ('produto_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
    ]
