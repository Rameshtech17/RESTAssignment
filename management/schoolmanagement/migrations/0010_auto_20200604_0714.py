# Generated by Django 3.0.6 on 2020-06-04 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0009_auto_20200604_0656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='Student',
            new_name='StudentName',
        ),
    ]