# Generated by Django 3.1.2 on 2020-11-06 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_resultslider_result_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mteacher',
        ),
        migrations.DeleteModel(
            name='sateacher',
        ),
        migrations.DeleteModel(
            name='steacher',
        ),
    ]
