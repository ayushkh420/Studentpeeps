# Generated by Django 3.2.5 on 2021-09-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
    ]