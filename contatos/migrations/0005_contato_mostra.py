# Generated by Django 3.1.2 on 2020-10-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_auto_20201003_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostra',
            field=models.BooleanField(default=True),
        ),
    ]