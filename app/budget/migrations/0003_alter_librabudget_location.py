# Generated by Django 3.2.13 on 2022-04-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_librabudget_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librabudget',
            name='location',
            field=models.CharField(choices=[('6 OCT', '6 OCTOBER'), ('ABO', 'ABOU AWAIKEL')], max_length=6),
        ),
    ]
