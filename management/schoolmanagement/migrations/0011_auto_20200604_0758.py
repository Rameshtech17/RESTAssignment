# Generated by Django 3.0.6 on 2020-06-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0010_auto_20200604_0714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='StudentName',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='Subject',
            new_name='Subject1',
        ),
        migrations.AddField(
            model_name='subject',
            name='Subject2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
