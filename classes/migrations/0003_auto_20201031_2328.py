# Generated by Django 3.1.2 on 2020-10-31 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='Education',
            new_name='education',
        ),
    ]