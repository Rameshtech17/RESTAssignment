# Generated by Django 3.0.6 on 2020-06-04 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0003_student_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='School',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schoolmanagement.School'),
        ),
    ]