# Generated by Django 3.0.6 on 2020-06-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0014_auto_20200604_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentslist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
            ],
        ),
    ]