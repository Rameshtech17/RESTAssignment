# Generated by Django 3.0.6 on 2020-06-05 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0026_auto_20200605_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolmanagement.Class'),
        ),
        migrations.AlterField(
            model_name='class',
            name='Student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolmanagement.StudentsList'),
        ),
    ]
