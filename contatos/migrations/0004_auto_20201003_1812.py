# Generated by Django 3.1.2 on 2020-10-03 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_auto_20201003_0324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='data_criação',
            new_name='data_da_criação',
        ),
    ]
