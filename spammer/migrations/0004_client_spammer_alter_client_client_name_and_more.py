# Generated by Django 5.0 on 2023-12-14 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spammer', '0003_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='spammer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spammer.spammer', verbose_name='ФИО менеджера'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=100, verbose_name='Имя клиента'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email клиента'),
        ),
    ]
