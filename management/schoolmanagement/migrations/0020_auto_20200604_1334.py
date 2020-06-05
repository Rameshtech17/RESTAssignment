# Generated by Django 3.0.6 on 2020-06-04 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0019_auto_20200604_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='Subject',
            new_name='Subject1',
        ),
        migrations.AddField(
            model_name='subject',
            name='Subject2',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='Students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolmanagement.StudentsList'),
        ),
    ]