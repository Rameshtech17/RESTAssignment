# Generated by Django 3.0.6 on 2020-06-04 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0021_auto_20200604_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='Students',
            new_name='StudentsList',
        ),
        migrations.AlterField(
            model_name='class',
            name='StudentsList',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolmanagement.StudentsList'),
        ),
    ]
