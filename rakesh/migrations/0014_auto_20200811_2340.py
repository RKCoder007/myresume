# Generated by Django 3.0.7 on 2020-08-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rakesh', '0013_auto_20200811_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myresumemodel',
            name='skill5_percentage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
