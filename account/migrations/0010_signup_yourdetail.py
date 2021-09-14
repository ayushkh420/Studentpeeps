# Generated by Django 3.2.5 on 2021-08-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_registers_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=1000)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Yourdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
        ),
    ]
