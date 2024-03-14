# Generated by Django 5.0.3 on 2024-03-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id_fornecedor', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá')], max_length=2)),
                ('cep', models.CharField(max_length=9)),
                ('contato', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('produtos', models.CharField(max_length=255)),
                ('tipo', models.CharField(blank=True, choices=[('CPF', 'CPF'), ('CNPJ', 'CNPJ')], max_length=4, null=True)),
            ],
        ),
    ]
