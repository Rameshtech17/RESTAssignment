# Generated by Django 3.0.6 on 2020-06-04 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0020_auto_20200604_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='Subject1',
            new_name='Subject',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='Subject2',
        ),
        migrations.AlterField(
            model_name='class',
            name='Students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolmanagement.StudentsList'),
        ),
    ]
