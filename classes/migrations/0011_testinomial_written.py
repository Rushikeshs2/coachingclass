# Generated by Django 3.1.2 on 2020-11-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0010_testinomial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testinomial',
            name='written',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
